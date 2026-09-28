# Business Analytics Job Market in China: Skills, Salary Levels, and AI-related Requirements in 2026

MGS4701 Business Analytics Group Project — Assignment 1 pilot.

## Project description

Research question: What skills, salary levels, and AI-related requirements are present in Business Analytics job postings in China in 2026?

This pilot organizes 100 BA-related public job posting excerpts to support descriptive work on advertised skills, salary ranges and AI-related requirements. The audience is WKU Business Analytics students choosing skills to study and roles to explore.

## Data source and collection period

Source: BOSS直聘. Collection method: Manual structured collection, with AI-assisted extraction and coding from public indexed posting cards. Collection date: 2026-09-28. The 100 records come from 28 public listing pages and 90 displayed company names. Detailed sources and selected IDs are recorded in data/source_manifest.csv.

The collection date is the inspection date, not a verified posting date. Indexed content can be older and pages can change. This file does not establish that every vacancy was first published in 2026 or is still open.

## Evidence and interpretation

Job_Description is a paraphrase of the visible JD excerpt, not the full JD. The URL identifies a public listing page and may recur for different jobs. AI_Required=1 means an AI-related task, tool, method or requirement appeared in the excerpt; it includes AI-related duties and does not establish mandatory proficiency. AI_Required=0 means none was visible in that excerpt. It is not verified absence from the complete JD. The human team review remains pending.

The purposive sample meets coverage targets of 40 data analyst, 20 business analyst, 20 BI and 20 operating-performance roles. It is not a probability sample. Role shares and the ten AI-positive excerpts must not be presented as nationwide market estimates or evidence of a causal salary premium.

## Files

| File | Contents |
| --- | --- |
| gbus_data.xlsx | Required four-sheet workbook and 100 records |
| 4701group.docx | Title page and project brief |
| data/BA_job_postings.csv | UTF-8 copy of the 15-field main table |
| data/coding_sheet.csv | Record-level role family, industry basis, AI coding basis and review status |
| data/pilot_extraction.json | Structured extraction snapshot used to assemble the main table |
| data/source_manifest.csv | 28 source pages and their selected record IDs |
| docs/CODING_RULES.md | AI, cleaning, role and industry rules |
| docs/COLLECTION_PROTOCOL.md | Search frame, first attempt, procedure and registered fallback |
| docs/AI_USE_LOG.md | AI assistance and human review responsibilities |
| scripts/validate_pilot.py | Re-runnable data-quality checks; Python standard library only |
| validation.ipynb | Executed notebook running the checks on the saved pilot |
| validation_summary.json | Results of the validation run |

## Variables explanation

| Variable | Type | Definition |
| --- | --- | --- |
| Job_ID | Text | Sequential record identifier, 001–100. Import as text to preserve leading zeros. |
| Job_Title | Text | Original displayed title; families are assigned separately in Coding_Rules. |
| Company | Text | Displayed recruiting company or brand name; not the platform name or necessarily the legal entity. |
| Industry | Category | Eight standardized sectors. Original labels and judgment-based mappings are retained in the coding sheet. |
| City | Category | Displayed work location: 北京、上海、杭州、深圳、广州. Ignore district names. |
| Salary | Text | Advertised monthly RMB range in K (1 K = RMB 1,000); preserve any stated number of salary payments. |
| Experience | Category | Experience requirement as displayed, including 经验不限. |
| Education | Category | Education requirement as displayed. |
| Skills | Text list | Semicolon-separated tools and competencies explicitly supported by the observed excerpt; not an exhaustive skill inventory. |
| Job_Description | Text | Short Chinese paraphrase of the publicly visible JD excerpt, prefixed 公开JD摘要. Not the complete JD. |
| AI_Required | Integer 0/1 | 1 = an AI-related task, tool, method or requirement is observed in the JD excerpt; 0 = none observed in that excerpt. |
| AI_Terms | Text list | Observed AI keywords separated by semicolons; use 未见（公开摘要） when AI_Required=0. |
| Source | Text | BOSS直聘 for every record. |
| Collection_Date | Date | 2026-09-28, the date of collection/inspection; not the original publication date. |
| URL | Text | Public BOSS listing page consulted. Not a unique job-detail permalink; pages may list several sampled jobs. |

## How to reproduce

1. Download or clone this repository and preserve its folder structure. Open gbus_data.xlsx; read README and Coding_Rules before interpreting the records. Import Job_ID as text if using CSV.
2. To reproduce the saved-pilot validation, run `python scripts/validate_pilot.py` from the repository root. Python 3.10 or later is sufficient; the script uses only the standard library. Alternatively, open validation.ipynb in Jupyter and run all cells. Jupyter is optional and is not a collection tool.
3. To repeat collection, follow docs/COLLECTION_PROTOCOL.md, starting with the recorded source pages and role/city keywords. Locate individual cards by company, title and city; do not infer facts from page titles. Use only accessible public information. Record a new collection date and any source changes.
4. Transcribe the visible fields, preserve salary notation, record industry evidence, paraphrase the excerpt and apply the coding rules. Log uncertain or missing evidence instead of filling it with assumptions. Apply the deduplication key and role targets, then assign IDs and re-run validation.
5. The stored JSON and CSV reproduce the selected dataset and its codes. Recollection cannot guarantee an identical sample because the public listing pages are dynamic and complete raw JDs were not archived.

## Team and submission status

LeiYongfeng: collection. WangYifei: cleaning and coding. Wangzhipeng: analysis and writing.

The local package includes the pilot, coding sheet, written protocol, README, AI log and brief. The title page still requires the team's actual GitHub repository URL. Upload all package contents to that repository before submission; creating this package does not satisfy the repository-upload requirement by itself. Independent source and coding review is still pending.
