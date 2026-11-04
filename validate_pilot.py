"""Validate the saved MGS4701 manual-collection pilot. Python standard library only."""
import csv
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
HEADERS = ['Job_ID','Job_Title','Company','Industry','City','Salary','Experience','Education','Skills','Job_Description','AI_Required','AI_Terms','Source','Collection_Date','URL']
EXPECTED_FAMILIES = {'数据分析师':40,'商业分析师':20,'BI分析师':20,'经营分析':20}
CITIES = {'北京','上海','杭州','深圳','广州'}
INDUSTRIES = {'互联网/科技','金融科技','电子商务','人工智能','制造业','新能源','物流','消费品'}
NEGATIVE = '未见（公开摘要）'

def read_csv(name):
    with (ROOT/'data'/name).open(encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f)
        return reader.fieldnames,list(reader)

def validate():
    head,rows=read_csv('BA_job_postings.csv')
    _,coding=read_csv('coding_sheet.csv')
    _,sources=read_csv('source_manifest.csv')
    norm=lambda s: re.sub(r'\s+','',s).casefold()
    keys=[tuple(norm(r[k]) for k in ['Company','Job_Title','City']) for r in rows]
    ai_bad=[]
    for r in rows:
        terms=r['AI_Terms']
        positive=r['AI_Required']=='1'
        ok=(positive and terms!=NEGATIVE) or (r['AI_Required']=='0' and terms==NEGATIVE)
        if positive:
            ok=ok and all(t.strip().casefold() in r['Job_Description'].casefold() for t in terms.split(';'))
        if not ok: ai_bad.append(r['Job_ID'])
    checks={
      'at_least_100_records':len(rows)>=100,
      'exact_required_columns':head==HEADERS,
      'no_empty_required_cells':all(all(str(r.get(k,'')).strip() for k in HEADERS) for r in rows),
      'sequential_text_ids':[r['Job_ID'] for r in rows]==[f'{i:03d}' for i in range(1,len(rows)+1)],
      'no_duplicate_company_title_city':len(keys)==len(set(keys)),
      'source_is_BOSS':all(r['Source']=='BOSS直聘' for r in rows),
      'company_is_not_platform':all(r['Company']!='BOSS直聘' for r in rows),
      'collection_date_matches':all(r['Collection_Date']=='2026-09-28' for r in rows),
      'five_cities_covered':{r['City'] for r in rows}==CITIES,
      'eight_industries_covered':{r['Industry'] for r in rows}==INDUSTRIES,
      'role_targets_met':dict(Counter(r['Role_Family'] for r in coding))==EXPECTED_FAMILIES,
      'coding_ids_match':[r['Job_ID'] for r in coding]==[r['Job_ID'] for r in rows],
      'ai_flag_term_summary_consistency':not ai_bad,
      'salary_format':all(re.fullmatch(r'\d+(?:\.\d+)?-\d+(?:\.\d+)?K(?:·\d+薪)?',r['Salary']) for r in rows),
      'BOSS_source_urls':all(urlparse(r['URL']).hostname in {'www.zhipin.com','m.zhipin.com'} for r in rows),
      'source_manifest_complete':{r['URL'] for r in rows}=={r['URL'] for r in sources} and sum(int(r['Selected_Records']) for r in sources)==len(rows),
    }
    report={'collection_date':'2026-09-28','rows':len(rows),'columns':len(head),'companies':len({r['Company'] for r in rows}),'source_pages':len(sources),'checks':checks,'all_checks_pass':all(checks.values()),'role_counts':dict(Counter(r['Role_Family'] for r in coding)),'city_counts':dict(Counter(r['City'] for r in rows)),'industry_counts':dict(Counter(r['Industry'] for r in rows)),'ai_counts':dict(Counter(r['AI_Required'] for r in rows)),'limitations':['Public indexed JD excerpts, not complete JDs.','AI=0 means no mention observed in the excerpt.','Posting dates and active vacancy status are unverified.','Independent human source review remains pending.','The GitHub URL and repository upload must be completed by the team.']}
    (ROOT/'validation_summary.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if not report['all_checks_pass']:
        raise AssertionError('Failed checks: '+', '.join(k for k,v in checks.items() if not v))
    return report

if __name__=='__main__':
    validate()
