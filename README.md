# TalentMiner v2 — Resume Parsing & Job Matching

*Parse. Match. Hire.*

TalentMiner parses resumes (PDF/DOCX) and Health Canada job descriptions, extracts skills,
scores every resume against every job with weighted fuzzy matching, loads the results into
Azure SQL, and serves them through a Streamlit app and a Power BI dashboard.

This folder is the **production-style reorganisation** of the Algonquin College capstone
project *HC Project 1 – Resume Scraping (Group 2)*. The originals are untouched in the parent
folder; every file's old and new location is listed in [`FILE_INDEX.md`](FILE_INDEX.md).

> ⚠️ **Security: do this first.** The v1 code (`archive/v1_original_code/Scripts/main.py`)
> has the Azure SQL username and password in plain text, and the same file is in the
> **public** GitHub repo `neetusco/resume-matching-python`. Rotate that password in Azure
> and remove it from the repo history. v2 reads credentials from a `.env` file instead.

---

## Folder structure

```
TalentMiner_v2/
├── README.md                  ← you are here
├── FILE_INDEX.md              ← every original file → its new location (or why it was skipped)
├── requirements.txt           ← Python dependencies (UTF-8; v1 file was UTF-16)
├── pyproject.toml             ← makes `src/talentminer` installable (pip install -e .)
├── .env.example               ← template for DB credentials → copy to .env
├── .gitignore
│
├── src/talentminer/           ← ACTIVE CODE (the pipeline)
│   ├── config/settings.py     ← all paths + settings in one place (path-safe, env-driven)
│   ├── parsers/
│   │   ├── resume_parser.py   ← resume → name, email, phone, education, title, skills
│   │   └── job_parser.py      ← job description → weighted skill list
│   ├── matching/matcher.py    ← resume × job weighted fuzzy match %
│   ├── database/db.py         ← Azure SQL connection, table creation, CSV loading
│   ├── utils/logging_utils.py
│   └── pipeline.py            ← entry point (was v1 Scripts/main.py)
│
├── app/streamlit_app.py       ← Streamlit UI (was v1 Scripts/app.py)
├── sql/schema.sql             ← database DDL (5 tables)
├── tests/                     ← pytest unit tests (starter set)
│
├── data/
│   ├── raw/resumes/           ← 23 pipeline input resumes
│   ├── raw/job_descriptions/  ← 17 Health Canada JDs
│   ├── reference/             ← job-title → skills lookup (drives both parsers)
│   ├── processed/             ← pipeline outputs (currently the v1 run of 2025-07-27)
│   ├── external/              ← Kaggle resume dataset (2,484 PDFs) + AI resume screening CSV
│   └── sample/                ← dummy/test CSVs and 2 non-Health-Canada sample JDs
│
├── dashboards/powerbi/        ← final .pbix + the cleaned CSV it was built on
├── assets/                    ← logo
├── logs/                      ← runtime error log (git-ignored)
│
├── docs/
│   ├── 01_project_management/ ← charter, kickoff list, project options, tracker
│   ├── 02_technical/          ← technical documentation, project links, v1 README & setup
│   ├── 03_final_deliverables/ ← final report + final presentation
│   └── 04_improvement_plan/   ← IMPROVEMENT_BACKLOG.md (start here for v2 work)
│
└── archive/                   ← history only — nothing here is used by the code
    ├── v1_original_code/      ← the exact code as submitted (reference)
    ├── v1_logs/               ← v1 development error log
    ├── prototypes/            ← early notebooks / scripts
    ├── prototype_outputs/     ← early CSV outputs and older skill-reference versions
    ├── old_test_inputs/       ← earlier resume/JD test sets (unique files only)
    ├── team_workspaces/prajna/← Prajna's draft deck, draft .pbix, extra resumes
    └── superseded_deliverables/← earlier drafts of the report / deck / .pbix
```

**Rule of thumb:** `src/`, `app/`, `sql/`, `data/raw`, `data/reference` are live.
`archive/` is read-only history.

---

## Pipeline flow

```
data/raw/resumes ──► resume_parser ──► data/processed/parsed_resumes.csv ──┐
                          ▲                                                 ├─► matcher ──► resume_match_results.csv ──► Azure SQL ──► Streamlit app
data/reference ───────────┤                                                 │                                              └──► Power BI
                          ▼                                                 │
data/raw/job_descriptions ► job_parser ──► data/processed/parsed_job_skills.csv
```

## Run it

```bash
# 1. Environment (Python 3.10+; Anaconda works too)
python -m venv .venv && .venv\Scripts\activate        # Windows
pip install -r requirements.txt
pip install -e .                                       # makes `talentminer` importable

# 2. Credentials (only needed for the database step / app)
copy .env.example .env      # then fill in DB_SERVER, DB_USER, DB_PASSWORD

# 3. Run
python -m talentminer.pipeline --no-db    # parse + match → CSVs in data/processed
python -m talentminer.pipeline            # same, plus load to Azure SQL
streamlit run app/streamlit_app.py        # UI (needs the database)
pytest                                    # unit tests
```

## What changed from v1

| Area | v1 | v2 |
|---|---|---|
| Layout | Code, data, drafts and deliverables mixed across root, `Archive/`, `Neetika/`, `Prajna/` | One project tree; live vs. archive separated |
| Duplicates | Same resumes in up to 3 folders; deliverables in both a folder and a .zip | Each unique file kept once (MD5 check) |
| Paths | Relative to the current folder; `input/other` vs. folder `Other` breaks on Linux/cloud | Anchored to project root in `settings.py` |
| Credentials | Hardcoded in `main.py` | `.env` (git-ignored) |
| Entry point | `Scripts/main.py` (always needs DB) | `python -m talentminer.pipeline [--no-db]` |
| Schema | Inline Python strings | `sql/schema.sql` |
| Tests | None | `tests/` (5 starter tests) |

**Parsing and matching logic is unchanged.** v2 produces the same parsed resumes, parsed job
skills and 391 match rows as the v1 run (verified row by row, ignoring row order and
skill-list order).

See [`docs/04_improvement_plan/IMPROVEMENT_BACKLOG.md`](docs/04_improvement_plan/IMPROVEMENT_BACKLOG.md)
for the issues found during the review and suggested next steps.

## Team (v1)

Neetika Upadhyay (Team Lead) · Prajna Ganji · Maruta Zalane · Shiva
