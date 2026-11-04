# Collection protocol

## Data source

BOSS直聘

## Keywords

数据分析师; 商业分析师; BI分析师; 经营分析; Business Analyst

## Additional terms

Data Analyst; BI Analyst; Business Intelligence Analyst; 商业数据分析; 经营数据分析; city/sector variants.

## Collection method

Manual structured collection

## Implementation

AI-assisted reading and structured transcription of public indexed BOSS posting cards. No automated scraper or access-control bypass; independent human review remains pending.

## Collection period

2026-09-28. Public indexed snapshots can predate this date; original posting dates were not available.

## Target and unit

One distinct job posting; purposive convenience sample of BA-related roles in five mainland Chinese cities.

## Role targets

数据分析师 40; 商业分析师 20; BI分析师 20; 经营分析 20. These are coverage targets, not estimates of market shares.

## City coverage

北京; 上海; 杭州; 深圳; 广州. Use the posting-card location, not the page title.

## Industry coverage

互联网/科技; 金融科技; 电子商务; 人工智能; 制造业; 新能源; 物流; 消费品.

## Step 1 Search

Search role keywords and city/sector variants; inspect public BOSS results. Do not select only AI-positive jobs.

## Step 2 Select

Check role relevance and essential fields against each visible card. Retain the original displayed company and title.

## Step 3 Record

Record salary, experience, education and location; extract supported skills, paraphrase the JD excerpt, and preserve the source URL.

## Step 4 Code

Apply Coding_Rules; record role family, original industry basis and AI evidence. Do not infer AI from employer industry alone.

## Step 5 Clean

Normalize text and categories, remove duplicate keys, sort by family, then assign IDs 001–100.

## Step 6 Validate

Run the supplied validation script or notebook; check all 15 fields, quotas, categories and AI consistency.

## First attempt outcome

100 selected unique records from 28 public listing pages. Job-detail access encountered verification barriers; full JDs were not collected. Total screened/excluded counts were not logged.

## Registered fallback

If BOSS cannot supply sufficient verifiable information, collect manually from Liepin, then Zhaopin, using the same schema. Record the actual source and report source changes. Neither fallback was used in this pilot.

## Reproduction limits

Re-running checks reproduces this saved pilot. A new website collection may differ because listings and search indexes change; links are listing pages, not permanent snapshots.

## Review before inference

Team members should inspect accessible full JDs and adjudicate AI coding before making claims about complete job requirements or nationwide 2026 prevalence.

