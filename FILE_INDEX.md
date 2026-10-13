# File Index — original location → TalentMiner_v2

Generated during the October 2026 reorganisation. Originals were **copied, not moved**; the parent folder is unchanged.
Files with identical content (MD5) were copied once. Later copies are listed as *duplicate of …*.

New files written for v2 (no v1 original): `README.md`, `FILE_INDEX.md`, `requirements.txt` (UTF-8 rewrite), `pyproject.toml`, `.env.example`, `.gitignore`, `src/talentminer/config/settings.py`, `src/talentminer/database/db.py`, `src/talentminer/pipeline.py`, `sql/schema.sql`, `tests/*`, `data/README.md`, `docs/04_improvement_plan/IMPROVEMENT_BACKLOG.md`.

Refactored from v1 (logic unchanged, imports and paths updated): `src/talentminer/parsers/resume_parser.py`, `parsers/job_parser.py`, `matching/matcher.py`, `utils/logging_utils.py`, `app/streamlit_app.py`. Exact v1 copies are in `archive/v1_original_code/`.


## Pipeline input

| Original | New location / status |
|---|---|
| `Neetika/project_root/input/resumes/Chemist -MAHIRA SHARMA.docx` | `data/raw/resumes/Chemist -MAHIRA SHARMA.docx` |
| `Neetika/project_root/input/resumes/Claire Morgan-Program officer.docx` | `data/raw/resumes/Claire Morgan-Program officer.docx` |
| `Neetika/project_root/input/resumes/Clara_Bennett_Senior_Program_Officer_Resume.docx` | `data/raw/resumes/Clara_Bennett_Senior_Program_Officer_Resume.docx` |
| `Neetika/project_root/input/resumes/Communications officer -KIMBERLY DUNN.docx` | `data/raw/resumes/Communications officer -KIMBERLY DUNN.docx` |
| `Neetika/project_root/input/resumes/Compliance Officer-NATASHA RIVERA.docx` | `data/raw/resumes/Compliance Officer-NATASHA RIVERA.docx` |
| `Neetika/project_root/input/resumes/Financial Clerk-Mark Chen.docx` | `data/raw/resumes/Financial Clerk-Mark Chen.docx` |
| `Neetika/project_root/input/resumes/Isabelle Tremblay_Biologist_Resume.pdf` | `data/raw/resumes/Isabelle Tremblay_Biologist_Resume.pdf` |
| `Neetika/project_root/input/resumes/Isabelle_Fournier_Senior_Digital_Communications_Resume.pdf` | `data/raw/resumes/Isabelle_Fournier_Senior_Digital_Communications_Resume.pdf` |
| `Neetika/project_root/input/resumes/Krishna_Korram_Senior_Program_Officer_Resume.pdf` | `data/raw/resumes/Krishna_Korram_Senior_Program_Officer_Resume.pdf` |
| `Neetika/project_root/input/resumes/Laboratory Chemist -DR Nathan.docx` | `data/raw/resumes/Laboratory Chemist -DR Nathan.docx` |
| `Neetika/project_root/input/resumes/Laboratory Technician -LAYLA IBRAHIM.docx` | `data/raw/resumes/Laboratory Technician -LAYLA IBRAHIM.docx` |
| `Neetika/project_root/input/resumes/Naresh_Kumar_Biologist_Section_Head_Resume.docx` | `data/raw/resumes/Naresh_Kumar_Biologist_Section_Head_Resume.docx` |
| `Neetika/project_root/input/resumes/Natasha_Gill_BI_Analyst_Tailored_Resume.docx` | `data/raw/resumes/Natasha_Gill_BI_Analyst_Tailored_Resume.docx` |
| `Neetika/project_root/input/resumes/Nathan_Brooks_Resume_Admin_Manager.docx` | `data/raw/resumes/Nathan_Brooks_Resume_Admin_Manager.docx` |
| `Neetika/project_root/input/resumes/Program Officer -CHANTAL RICHARD.docx` | `data/raw/resumes/Program Officer -CHANTAL RICHARD.docx` |
| `Neetika/project_root/input/resumes/Program Officer -SOPHIE LEVESQUE.docx` | `data/raw/resumes/Program Officer -SOPHIE LEVESQUE.docx` |
| `Neetika/project_root/input/resumes/Program Officer-Jason.docx` | `data/raw/resumes/Program Officer-Jason.docx` |
| `Neetika/project_root/input/resumes/Ravi_Sharma_Senior_BI_Analyst_Resume.pdf` | `data/raw/resumes/Ravi_Sharma_Senior_BI_Analyst_Resume.pdf` |
| `Neetika/project_root/input/resumes/Regulatory Compliance and Enforcement Officer-CHRISTOPHER HANSON.docx` | `data/raw/resumes/Regulatory Compliance and Enforcement Officer-CHRISTOPHER HANSON.docx` |
| `Neetika/project_root/input/resumes/Senior Communication addvisor-MARISA TORRES.docx` | `data/raw/resumes/Senior Communication addvisor-MARISA TORRES.docx` |
| `Neetika/project_root/input/resumes/Senior Financial Clerk -ANNE LEBLANC.docx` | `data/raw/resumes/Senior Financial Clerk -ANNE LEBLANC.docx` |
| `Neetika/project_root/input/resumes/Senior Program Officer-Daniella.docx` | `data/raw/resumes/Senior Program Officer-Daniella.docx` |
| `Neetika/project_root/input/resumes/Sophia_Clarke_Resume_Administrative_officer.docx` | `data/raw/resumes/Sophia_Clarke_Resume_Administrative_officer.docx` |
| `Neetika/project_root/input/job_descriptions/Administrative Officer.docx` | `data/raw/job_descriptions/Administrative Officer.docx` |
| `Neetika/project_root/input/job_descriptions/Biologist.docx` | `data/raw/job_descriptions/Biologist.docx` |
| `Neetika/project_root/input/job_descriptions/Business Intelligence Analyst.docx` | `data/raw/job_descriptions/Business Intelligence Analyst.docx` |
| `Neetika/project_root/input/job_descriptions/Communications Officer.docx` | `data/raw/job_descriptions/Communications Officer.docx` |
| `Neetika/project_root/input/job_descriptions/Data Analyst.docx` | `data/raw/job_descriptions/Data Analyst.docx` |
| `Neetika/project_root/input/job_descriptions/Finance Clerk.docx` | `data/raw/job_descriptions/Finance Clerk.docx` |
| `Neetika/project_root/input/job_descriptions/Finance Officer.docx` | `data/raw/job_descriptions/Finance Officer.docx` |
| `Neetika/project_root/input/job_descriptions/HR Advisor.docx` | `data/raw/job_descriptions/HR Advisor.docx` |
| `Neetika/project_root/input/job_descriptions/IT Manager.docx` | `data/raw/job_descriptions/IT Manager.docx` |
| `Neetika/project_root/input/job_descriptions/Laboratory Chemist II.docx` | `data/raw/job_descriptions/Laboratory Chemist II.docx` |
| `Neetika/project_root/input/job_descriptions/Manager- Data Science & Analytics.docx` | `data/raw/job_descriptions/Manager- Data Science & Analytics.docx` |
| `Neetika/project_root/input/job_descriptions/Policy Analyst.docx` | `data/raw/job_descriptions/Policy Analyst.docx` |
| `Neetika/project_root/input/job_descriptions/Program Officer.docx` | `data/raw/job_descriptions/Program Officer.docx` |
| `Neetika/project_root/input/job_descriptions/Regional Regulatory Compliance and Enforcement Officer.docx` | `data/raw/job_descriptions/Regional Regulatory Compliance and Enforcement Officer.docx` |
| `Neetika/project_root/input/job_descriptions/Senior Communications Advisor.docx` | `data/raw/job_descriptions/Senior Communications Advisor.docx` |
| `Neetika/project_root/input/job_descriptions/Senior Financial Clerk.docx` | `data/raw/job_descriptions/Senior Financial Clerk.docx` |
| `Neetika/project_root/input/job_descriptions/Senior Program Officer.docx` | `data/raw/job_descriptions/Senior Program Officer.docx` |
| `Neetika/project_root/input/Other/Health_Canada_Jobs_With_Skills_1.csv` | `data/reference/health_canada_jobs_with_skills.csv` |
| `Neetika/project_root/input/Other/Health_Canada_Jobs_With_Skills_1.xlsx` | `data/reference/health_canada_jobs_with_skills.xlsx` |

## Pipeline output (v1 run 2025-07-27)

| Original | New location / status |
|---|---|
| `Neetika/project_root/output/parsed_resumes.csv` | `data/processed/parsed_resumes.csv` |
| `Neetika/project_root/output/parsed_job_skills.csv` | `data/processed/parsed_job_skills.csv` |
| `Neetika/project_root/output/resume_match_results.csv` | `data/processed/resume_match_results.csv` |
| `Neetika/project_root/last_update.txt` | `data/processed/last_update.txt` |

## Assets

| Original | New location / status |
|---|---|
| `Neetika/project_root/assets/TalentMiner_logo.png` | `assets/TalentMiner_logo.png` |

## External data

| Original | New location / status |
|---|---|
| `Archive/data/data/  (24 category folders, 2,484 PDFs)` | `data/external/kaggle_resume_dataset/  (2484 files copied)` |
| `AI_Resume_Screening.csv` | `data/external/ai_resume_screening.csv` |

## Sample / dummy data

| Original | New location / status |
|---|---|
| `dummy_resume_data.csv` | `data/sample/dummy_resume_data.csv` |
| `jd_parsing_dummy.csv` | `data/sample/dummy_jd_parsing.csv` |
| `matching_result_weighted_dummy.csv` | `data/sample/dummy_matching_result_weighted.csv` |
| `candidates_info (1).xls` | `data/sample/candidates_info.csv` |
| `1_New JD.docx` | `data/sample/job_descriptions/Financial_Services_Sales_JD.docx` |
| `Archive/Job Description.docx` | `data/sample/job_descriptions/Medical_Laboratory_Technologist_JD.docx` |

## Dashboards

| Original | New location / status |
|---|---|
| `Capstone Project Deliverable/PowerBI - HC Project 1 - Resume Scraping - Group2.pbix` | `dashboards/powerbi/TalentMiner_Dashboard_FINAL.pbix` |
| `Prajna/Resume_Scraping_Dashboard_Cleaned.csv` | `dashboards/powerbi/data/resume_scraping_dashboard_cleaned.csv` |

## Docs

| Original | New location / status |
|---|---|
| `Archive/Kickoff/Group2- Project Charter – HC Project 1 - Resume Scraping.pdf` | `docs/01_project_management/Project_Charter.pdf` |
| `Archive/Kickoff/Capstone Project - for kick off.xlsx` | `docs/01_project_management/Kickoff_Project_List.xlsx` |
| `Archive/Kickoff/Resume_Capstone_Project_Options.docx` | `docs/01_project_management/Project_Options.docx` |
| `Project Tracker.xlsx` | `docs/01_project_management/Project_Tracker.xlsx` |
| `Capstone Project Deliverable/Technical Documentation - HC Project 1 - Resume Scraping - Group2.docx` | `docs/02_technical/Technical_Documentation.docx` |
| `Capstone Project Deliverable/Project file with datasets - HC Project 1 - Resume Scraping - Group2.docx` | `docs/02_technical/Project_Links_GitHub_PowerBI_Streamlit.docx` |
| `Neetika/project_root/environment_setup_instructions.txt` | `docs/02_technical/v1_environment_setup_instructions.txt` |
| `Neetika/project_root/README.md` | `docs/02_technical/v1_README.md` |
| `Capstone Project Deliverable/Final Report - HC Project 1 - Resume Scraping - Group2.docx` | `docs/03_final_deliverables/Final_Report.docx` |
| `Capstone Project Deliverable/Presentation - HC Project 1 - Resume Scraping - Group2.pptx` | `docs/03_final_deliverables/Final_Presentation.pptx` |
| `HC Project 1 - Resume Scraping - Group2 - Deliverable.zip` | not copied: holds the same 5 files as `Capstone Project Deliverable/` (identical sizes); see `docs/03_final_deliverables/` and `dashboards/powerbi/` |

## Archive - v1 code (as submitted)

| Original | New location / status |
|---|---|
| `Neetika/project_root/Scripts/app.py` | `archive/v1_original_code/Scripts/app.py` |
| `Neetika/project_root/Scripts/job_parser.py` | `archive/v1_original_code/Scripts/job_parser.py` |
| `Neetika/project_root/Scripts/main.py` | `archive/v1_original_code/Scripts/main.py` |
| `Neetika/project_root/Scripts/matcher.py` | `archive/v1_original_code/Scripts/matcher.py` |
| `Neetika/project_root/Scripts/resume_parser.py` | `archive/v1_original_code/Scripts/resume_parser.py` |
| `Neetika/project_root/Scripts/settings.py` | `archive/v1_original_code/Scripts/settings.py` |
| `Neetika/project_root/Scripts/utils.py` | `archive/v1_original_code/Scripts/utils.py` |
| `Neetika/project_root/Scripts/__init__.py` | `archive/v1_original_code/Scripts/__init__.py` |
| `Neetika/project_root/requirements.txt` | `archive/v1_original_code/requirements.txt` |
| `job_parser.py` | duplicate of `archive/v1_original_code/Scripts/job_parser.py` |
| `resume_parser.py` | duplicate of `archive/v1_original_code/Scripts/resume_parser.py` |
| `Neetika/project_root/output/logs/errors.log` | `archive/v1_logs/errors.log` |

## Archive - prototypes

| Original | New location / status |
|---|---|
| `Archive/test.py` | `archive/prototypes/main_local_sqlserver_version.py` |
| `Archive/resume_parsing/skill_parsing2 (1).py` | `archive/prototypes/skill_parsing2.py` |
| `Neetika/Archive/skill_parsing2.py` | duplicate of `archive/prototypes/skill_parsing2.py` |
| `Archive/resume_parsing/version4 (2).ipynb` | `archive/prototypes/resume_parser_version4.ipynb` |
| `Neetika/Archive/version4 (2).py` | duplicate of `archive/prototypes/resume_parser_version4.ipynb` |
| `Archive/Resume_info_scraping.ipynb` | `archive/prototypes/Resume_info_scraping.ipynb` |
| `Archive/Resume_info_scraping-Copy1.ipynb` | `archive/prototypes/Resume_info_scraping_copy1.ipynb` |
| `Archive/test code.docx` | `archive/prototypes/jd_parser_tfidf_spacy_code.docx` |

## Archive - prototype outputs

| Original | New location / status |
|---|---|
| `Archive/parsed_job_skills.csv` | `archive/prototype_outputs/parsed_job_skills.csv` |
| `Archive/parsed_resumes.csv` | `archive/prototype_outputs/parsed_resumes.csv` |
| `Archive/resume_match_results.csv` | `archive/prototype_outputs/resume_match_results.csv` |
| `Archive/resume_parsing/parsed_resume (2).xls` | `archive/prototype_outputs/parsed_resume_early.csv` |
| `Archive/Health_Canada_Jobs_With_Skills_1.csv` | `archive/prototype_outputs/health_canada_jobs_with_skills_early_v1.csv` |
| `Neetika/Archive/Health_Canada_Jobs_With_Skills_1.csv` | `archive/prototype_outputs/health_canada_jobs_with_skills_early_v2.csv` |
| `Archive/resume_parsing/Health_Canada_Jobs_With_Skills_1.xls` | `archive/prototype_outputs/health_canada_jobs_with_skills_early_v1.xls` |
| `Neetika/Archive/input/Other/Health_Canada_Jobs_With_Skills_1.csv` | duplicate of `archive/prototype_outputs/health_canada_jobs_with_skills_early_v1.csv` |

## Archive - old test inputs

| Original | New location / status |
|---|---|
| `Neetika/Archive/input/resumes/Business_Development_Manager_Resume.pdf` | `archive/old_test_inputs/resumes/Business_Development_Manager_Resume.pdf` |
| `Neetika/Archive/input/resumes/Data_Scientist_Resume.pdf` | `archive/old_test_inputs/resumes/Data_Scientist_Resume.pdf` |
| `Neetika/Archive/input/resumes/Medical_Assistant_Resume.pdf` | `archive/old_test_inputs/resumes/Medical_Assistant_Resume.pdf` |
| `Neetika/Archive/input/resumes/Medical_Assistant_Resume_Updated.pdf` | `archive/old_test_inputs/resumes/Medical_Assistant_Resume_Updated.pdf` |
| `Neetika/Archive/input/resumes/Medical_Receptionist_Resume.pdf` | `archive/old_test_inputs/resumes/Medical_Receptionist_Resume.pdf` |
| `Neetika/Archive/input/resumes/Modern nursing resume.docx` | `archive/old_test_inputs/resumes/Modern nursing resume.docx` |
| `Neetika/Archive/input/resumes/Paramedic_Resume.pdf` | `archive/old_test_inputs/resumes/Paramedic_Resume.pdf` |
| `Neetika/Archive/input/resumes/Retail_Manager_Resume.pdf` | `archive/old_test_inputs/resumes/Retail_Manager_Resume.pdf` |
| `Neetika/Archive/input/resumes/Simple healthcare resume.docx` | `archive/old_test_inputs/resumes/Simple healthcare resume.docx` |
| `Neetika/Archive/input/resumes/Skills focus graphic professional resume.docx` | `archive/old_test_inputs/resumes/Skills focus graphic professional resume.docx` |
| `Neetika/Archive/input/resumes/Stylish teaching resume.docx` | `archive/old_test_inputs/resumes/Stylish teaching resume.docx` |
| `Neetika/Archive/resumes/Administrative_Assistant_Resume.pdf` | `archive/old_test_inputs/resumes/Administrative_Assistant_Resume.pdf` |
| `Neetika/Archive/resumes/Biologist_Resume.pdf` | duplicate of `data/raw/resumes/Isabelle Tremblay_Biologist_Resume.pdf` |
| `Neetika/Archive/resumes/Claire Morgan-Program officer.docx` | duplicate of `data/raw/resumes/Claire Morgan-Program officer.docx` |
| `Neetika/Archive/resumes/Communications_Officer_Resume.pdf` | `archive/old_test_inputs/resumes/Communications_Officer_Resume.pdf` |
| `Neetika/Archive/resumes/Data Analyst_Resume.docx` | `archive/old_test_inputs/resumes/Data Analyst_Resume.docx` |
| `Neetika/Archive/resumes/Financial Analyst.pdf` | `archive/old_test_inputs/resumes/Financial Analyst.pdf` |
| `Neetika/Archive/resumes/Financial_Analyst_Resume.docx` | `archive/old_test_inputs/resumes/Financial_Analyst_Resume.docx` |
| `Neetika/Archive/resumes/Human_Resources_Advisor_Resumed.docx` | `archive/old_test_inputs/resumes/Human_Resources_Advisor_Resumed.docx` |
| `Neetika/Archive/resumes/IT_Professional_Resume_Updated.docx` | `archive/old_test_inputs/resumes/IT_Professional_Resume_Updated.docx` |
| `Neetika/Archive/resumes/Inspection_and_Compliance_Officer_Resume.docx` | `archive/old_test_inputs/resumes/Inspection_and_Compliance_Officer_Resume.docx` |
| `Neetika/Archive/resumes/Laboratory_Scientist_Resume.pdf` | `archive/old_test_inputs/resumes/Laboratory_Scientist_Resume.pdf` |
| `Neetika/Archive/resumes/Medical_Officer_Resume.pdf` | `archive/old_test_inputs/resumes/Medical_Officer_Resume.pdf` |
| `Neetika/Archive/resumes/Policy_Analyst_Resume_Health_Canada.docx` | `archive/old_test_inputs/resumes/Policy_Analyst_Resume_Health_Canada.docx` |
| `Neetika/Archive/resumes/Program Officer -CHANTAL RICHARD.docx` | duplicate of `data/raw/resumes/Program Officer -CHANTAL RICHARD.docx` |
| `Neetika/Archive/resumes/Program Officer -SOPHIE LEVESQUE.docx` | duplicate of `data/raw/resumes/Program Officer -SOPHIE LEVESQUE.docx` |
| `Neetika/Archive/resumes/Program Officer-Jason.docx` | duplicate of `data/raw/resumes/Program Officer-Jason.docx` |
| `Neetika/Archive/resumes/Project Management Coordinator.docx` | `archive/old_test_inputs/resumes/Project Management Coordinator.docx` |
| `Neetika/Archive/resumes/Regulatory Compliance and Enforcement Officer-CHRISTOPHER HANSON.docx` | duplicate of `data/raw/resumes/Regulatory Compliance and Enforcement Officer-CHRISTOPHER HANSON.docx` |
| `Neetika/Archive/resumes/Regulatory Compliance and Enforcement Officer-NATASHA RIVERA.docx` | `archive/old_test_inputs/resumes/Regulatory Compliance and Enforcement Officer-NATASHA RIVERA.docx` |
| `Neetika/Archive/resumes/Resume_IT Analyst.docx` | `archive/old_test_inputs/resumes/Resume_IT Analyst.docx` |
| `Neetika/Archive/resumes/Section Head-TAMARA GRIFFIN.docx` | `archive/old_test_inputs/resumes/Section Head-TAMARA GRIFFIN.docx` |
| `Neetika/Archive/resumes/Section head-Dr.Ayesha Parmar.docx` | `archive/old_test_inputs/resumes/Section head-Dr.Ayesha Parmar.docx` |
| `Neetika/Archive/resumes/Section head-JULIEN LECLAIR.docx` | `archive/old_test_inputs/resumes/Section head-JULIEN LECLAIR.docx` |
| `Neetika/Archive/resumes/Senior Communication addvisor-MARISA TORRES.docx` | duplicate of `data/raw/resumes/Senior Communication addvisor-MARISA TORRES.docx` |
| `Neetika/Archive/resumes/Senior Communications Advisor -KIMBERLY DUNN.docx` | `archive/old_test_inputs/resumes/Senior Communications Advisor -KIMBERLY DUNN.docx` |
| `Neetika/Archive/resumes/Senior Financial Clerk -ANNE LEBLANC.docx` | `archive/old_test_inputs/resumes/Senior Financial Clerk -ANNE LEBLANC.docx` |
| `Neetika/Archive/resumes/Senior Financial Clerk-Mark Chen.docx` | `archive/old_test_inputs/resumes/Senior Financial Clerk-Mark Chen.docx` |
| `Neetika/Archive/resumes/Senior Program Officer-Daniella.docx` | duplicate of `data/raw/resumes/Senior Program Officer-Daniella.docx` |
| `Archive/resume_parsing/resumes parsed/Community Health Nurse.docx` | `archive/old_test_inputs/resumes/Community Health Nurse.docx` |
| `Archive/resume_parsing/resumes parsed/Financial Analyst.docx` | `archive/old_test_inputs/resumes/Financial Analyst.docx` |
| `Archive/resume_parsing/resumes parsed/Financial Analyst.pdf` | duplicate of `archive/old_test_inputs/resumes/Financial Analyst.pdf` |
| `Archive/resume_parsing/resumes parsed/Project Management Coordinator.docx` | duplicate of `archive/old_test_inputs/resumes/Project Management Coordinator.docx` |
| `Archive/resume_parsing/resumes parsed/sample.resume.docx` | duplicate of `archive/old_test_inputs/resumes/Resume_IT Analyst.docx` |
| `Neetika/Archive/input/job_descriptions/CLGYJP00000330 Business Intelligence and Analytics Analyst 13.docx` | `archive/old_test_inputs/job_descriptions/CLGYJP00000330 Business Intelligence and Analytics Analyst 13.docx` |
| `Neetika/Archive/input/job_descriptions/HealthCanada_JobDescriptions.pdf` | `archive/old_test_inputs/job_descriptions/HealthCanada_JobDescriptions.pdf` |
| `Neetika/Archive/input/job_descriptions/Job title-101_Data Analyst.docx` | `archive/old_test_inputs/job_descriptions/Job title-101_Data Analyst.docx` |
| `Neetika/Archive/input/HealthCanada_JobDescriptions.pdf` | duplicate of `archive/old_test_inputs/job_descriptions/HealthCanada_JobDescriptions.pdf` |

## Archive - team workspaces

| Original | New location / status |
|---|---|
| `Prajna/Resumes/Claire Morgan-Program officer.docx` | duplicate of `data/raw/resumes/Claire Morgan-Program officer.docx` |
| `Prajna/Resumes/Claire_Morgan_Senior_Program_Officer_Resume_Updated.docx` | `archive/team_workspaces/prajna/resumes/Claire_Morgan_Senior_Program_Officer_Resume_Updated.docx` |
| `Prajna/Resumes/Compliance Officer-NATASHA RIVERA.docx` | duplicate of `data/raw/resumes/Compliance Officer-NATASHA RIVERA.docx` |
| `Prajna/Resumes/HR_Advisor_Resume_HealthCanada.docx` | `archive/team_workspaces/prajna/resumes/HR_Advisor_Resume_HealthCanada.docx` |
| `Prajna/Resumes/IT MANAGER-MOHAMED ALI.docx` | `archive/team_workspaces/prajna/resumes/IT MANAGER-MOHAMED ALI.docx` |
| `Prajna/Resumes/IT MANAGER-eMILIE.docx` | `archive/team_workspaces/prajna/resumes/IT MANAGER-eMILIE.docx` |
| `Prajna/Resumes/IT Manager-CARLOS MORALES.docx` | `archive/team_workspaces/prajna/resumes/IT Manager-CARLOS MORALES.docx` |
| `Prajna/Resumes/Isabelle Tremblay_Biologist_Resume.pdf` | duplicate of `data/raw/resumes/Isabelle Tremblay_Biologist_Resume.pdf` |
| `Prajna/Resumes/Isabelle_Fournier_Senior_Digital_Communications_Resume.pdf` | duplicate of `data/raw/resumes/Isabelle_Fournier_Senior_Digital_Communications_Resume.pdf` |
| `Prajna/Resumes/Krishna_Korram_Senior_Program_Officer_Resume.pdf` | duplicate of `data/raw/resumes/Krishna_Korram_Senior_Program_Officer_Resume.pdf` |
| `Prajna/Resumes/Laboratory Chemist -DR Nathan.docx` | duplicate of `data/raw/resumes/Laboratory Chemist -DR Nathan.docx` |
| `Prajna/Resumes/Laboratory Chemist -LAYLA IBRAHIM.docx` | `archive/team_workspaces/prajna/resumes/Laboratory Chemist -LAYLA IBRAHIM.docx` |
| `Prajna/Resumes/Laboratory Chemist -MAHIRA SHARMA.docx` | `archive/team_workspaces/prajna/resumes/Laboratory Chemist -MAHIRA SHARMA.docx` |
| `Prajna/Resumes/Naresh_Kumar_Biologist_Section_Head_Resume.docx` | `archive/team_workspaces/prajna/resumes/Naresh_Kumar_Biologist_Section_Head_Resume.docx` |
| `Prajna/Resumes/Natasha_Gill_BI_Analyst_Tailored_Resume.docx` | `archive/team_workspaces/prajna/resumes/Natasha_Gill_BI_Analyst_Tailored_Resume.docx` |
| `Prajna/Resumes/Nathan_Brooks_Resume_Admin_Officer.docx` | `archive/team_workspaces/prajna/resumes/Nathan_Brooks_Resume_Admin_Officer.docx` |
| `Prajna/Resumes/Program Officer -CHANTAL RICHARD.docx` | duplicate of `data/raw/resumes/Program Officer -CHANTAL RICHARD.docx` |
| `Prajna/Resumes/Program Officer -SOPHIE LEVESQUE.docx` | duplicate of `data/raw/resumes/Program Officer -SOPHIE LEVESQUE.docx` |
| `Prajna/Resumes/Program Officer-Jason.docx` | duplicate of `data/raw/resumes/Program Officer-Jason.docx` |
| `Prajna/Resumes/Ravi_Sharma_Senior_BI_Analyst_Resume.pdf` | duplicate of `data/raw/resumes/Ravi_Sharma_Senior_BI_Analyst_Resume.pdf` |
| `Prajna/Resumes/Regulatory Compliance and Enforcement Officer-CHRISTOPHER HANSON.docx` | duplicate of `data/raw/resumes/Regulatory Compliance and Enforcement Officer-CHRISTOPHER HANSON.docx` |
| `Prajna/Resumes/Senior Communication addvisor-MARISA TORRES.docx` | duplicate of `data/raw/resumes/Senior Communication addvisor-MARISA TORRES.docx` |
| `Prajna/Resumes/Senior Communications Advisor -KIMBERLY DUNN.docx` | duplicate of `archive/old_test_inputs/resumes/Senior Communications Advisor -KIMBERLY DUNN.docx` |
| `Prajna/Resumes/Senior Financial Clerk -ANNE LEBLANC.docx` | duplicate of `archive/old_test_inputs/resumes/Senior Financial Clerk -ANNE LEBLANC.docx` |
| `Prajna/Resumes/Senior Financial Clerk-Mark Chen.docx` | `archive/team_workspaces/prajna/resumes/Senior Financial Clerk-Mark Chen.docx` |
| `Prajna/Resumes/Senior Program Officer-Daniella.docx` | duplicate of `data/raw/resumes/Senior Program Officer-Daniella.docx` |
| `Prajna/Resumes/Sophia_Clarke_Resume_Admin_Officer.pdf` | `archive/team_workspaces/prajna/resumes/Sophia_Clarke_Resume_Admin_Officer.pdf` |
| `Prajna/cape stone final.pptx` | `archive/team_workspaces/prajna/capstone_final_draft.pptx` |
| `Prajna/cape stone power bi.pbix` | `archive/team_workspaces/prajna/capstone_powerbi_draft.pbix` |

## Archive - superseded deliverables

| Original | New location / status |
|---|---|
| `Presentation - HC Project 1 - Resume Scraping - Group2.pptx` | `archive/superseded_deliverables/Presentation_draft_root.pptx` |
| `HC cape stone - Resume Scraping - Group2.pptx` | `archive/superseded_deliverables/Presentation_draft_hc_capstone.pptx` |
| `Archive/HC Project 1 - Resume Scraping - Group2.pptx` | `archive/superseded_deliverables/Presentation_draft_archive.pptx` |
| `Archive/Report - HC Project 1 - Resume Scraping - Group2.docx` | `archive/superseded_deliverables/Report_draft.docx` |
| `Archive/Final Power Bi_older.pbix` | `archive/superseded_deliverables/PowerBI_older.pbix` |

## Not copied

| Original | New location / status |
|---|---|
| `Neetika/project_root/.git/` | not copied: git history of github.com/neetusco/resume-matching-python (contains the old hardcoded DB password) |
| `Neetika/project_root/**/__pycache__/` | not copied: compiled Python cache, regenerated automatically |
