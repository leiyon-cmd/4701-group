# Coding rules

| Area | Rule | Definition |
| --- | --- | --- |
| AI coding | Scope | Code only the observed JD excerpt. AI_Required is a broad mention indicator, including AI-related duties; it does not establish mandatory AI proficiency. |
| AI coding | Positive = 1 | An explicit AI tool, method or AI-related work requirement occurs in the excerpt. Examples include AI, ChatGPT, LLM, 大模型, AIGC, Generative AI, 机器学习, and AI-context Agent/NLP terms. |
| AI coding | Negative = 0 | No qualifying AI requirement is visible in the excerpt. Write AI_Terms as 未见（公开摘要）. Do not interpret this as verified absence from the full JD. |
| AI coding | Context review | Company industry 人工智能, generic Python, SQL, data mining, BI, automation or RPA alone do not trigger 1. Agent, 情感分析 and 意图识别 require AI/technical context. |
| AI coding | Terms | Retain the observed keyword, normalize English case where useful, remove repeats, and separate terms with semicolons. Do not add unobserved ChatGPT/LLM examples. |
| AI coding | Consistency | Every positive must have a concrete keyword supported by its summary. Every negative uses the standard nonempty sentinel. Keep ambiguous cases for team review. |
| Cleaning | Inclusion | A relevant analytical role in one of the five cities, with company, salary, experience, education, industry evidence and a useful public JD excerpt. |
| Cleaning | Exclusion | Exclude unrelated roles, locations outside the frame, missing essential source information, obscured company names and duplicate company-title-city combinations. |
| Cleaning | Identifiers | Assign text IDs 001–100 after selection and deduplication. Sort by the four role families; retain original titles. |
| Cleaning | Duplicate rule | Normalize spaces and English case in company, title and city. Keep one record for the same key; distinct roles at the same company remain separate. |
| Cleaning | No imputation | Do not fabricate absent salaries, qualifications, tools or employer names. 经验不限 is an observed category, not missing data. |
| Cleaning | Skills and JD | Extract supported skills; normalize SQL/Python/Power BI names. Summarize observed duties in Chinese without presenting the summary as a full quotation. |
| Cleaning | Salary | Preserve the original monthly range and any 13/14/15/16/17薪 suffix. Do not infer 12 payments when the suffix is absent. |
| Cleaning | City | Use the location shown in the individual posting card, even if the listing-page title names another city. |
| Cleaning | Industry | Map source company-sector labels to eight sectors. Log explicit business-unit overrides and same-company supporting pages in the record-level coding sheet. |
| Cleaning | Source and date | Source=BOSS直聘; Collection_Date=2026-09-28. Listing URLs may repeat across different jobs. Original posting dates and current active status are not verified. |
| Cleaning | Validation | Check 100 rows, 15 required fields, sequential IDs, zero empty cells, duplicate keys, all five cities/eight sectors, and AI flag-term consistency. |
| Review | Human review | AI-assisted extraction and coding are complete. Independent team checking is pending; collection and cleaning owners should resolve any discrepancies against accessible source evidence. |

## Role families

| Family | Target | Definition |
| --- | --- | --- |
| 数据分析师 | 40 | Data analyst and analytics specialist roles focused on data interpretation, product, user, risk or business analysis. |
| 商业分析师 | 20 | Commercial/business analysis roles, including 商业数据分析 and specialist/manager variants. |
| BI分析师 | 20 | BI/商业智能 analysis, reporting, dashboard, BI requirements or development roles with an explicit analytical component. Includes one Power BI-centered data analyst. |
| 经营分析 | 20 | Operating performance, planning, budgeting and management analysis. Includes a data analyst explicitly focused on 经营分析. |

## Industry mapping

| Industry | Source labels | Interpretation |
| --- | --- | --- |
| 互联网/科技 | 互联网; 计算机软件; 大数据; 游戏; 移动互联网; 汽车智能网联 | Use the displayed broad company sector unless an explicit business-unit override is recorded. |
| 金融科技 | 互联网金融; explicitly identified digital financial business | Overrides: 蚂蚁集团钱塘征信、平安银行、度小满. These are research classifications, not claims about legal licensing. |
| 电子商务 | 电子商务 | Retain this category where shown, even when the company sells consumer goods. |
| 人工智能 | 人工智能 | Company-sector classification alone does not imply AI_Required=1. |
| 制造业 | 智能硬件; 消费电子; 电子/硬件开发; 家具/家居; 家用电器; 通信/网络设备 | Broader analytical grouping of hardware and manufacturing sectors. |
| 新能源 | 风电; 新能源; 新能源汽车 | Explicit business-unit override for 小米汽车电动汽车岗位. |
| 物流 | 物流/仓储; 快递; 跨境物流; 公路物流 | Logistics and warehousing grouping. |
| 消费品 | 批发/零售; 新零售; 日化; 服装/纺织; 食品/饮料/烟酒 | Consumer products and associated retail grouping. |

The record-level coding sheet is data/coding_sheet.csv. The Evidence_Scope field applies to every observation; Team_Review_Status does not claim that an independent reviewer has checked a record.
