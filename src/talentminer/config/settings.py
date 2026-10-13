"""Central configuration for TalentMiner.

All paths are anchored to the project root, so the pipeline works no matter
which folder you run it from (v1 relied on the current working directory).
Secrets (database credentials) come from environment variables / a local
.env file - never hardcode them here.
"""
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Load .env if python-dotenv is installed (optional)
try:
    from dotenv import load_dotenv
    load_dotenv(PROJECT_ROOT / ".env")
except ImportError:
    pass

DATA_DIR = PROJECT_ROOT / "data"

# ---- Inputs ----
RESUME_FOLDER = str(DATA_DIR / "raw" / "resumes")
JD_FOLDER = str(DATA_DIR / "raw" / "job_descriptions")
KEYWORDS_FILE = str(DATA_DIR / "reference" / "health_canada_jobs_with_skills.csv")

# ---- Outputs ----
PROCESSED_DIR = DATA_DIR / "processed"
PARSED_RESUMES_FILE = str(PROCESSED_DIR / "parsed_resumes.csv")
PARSED_JD_FILE = str(PROCESSED_DIR / "parsed_job_skills.csv")
MATCH_RESULTS_FILE = str(PROCESSED_DIR / "resume_match_results.csv")
LAST_UPDATE_FILE = str(PROCESSED_DIR / "last_update.txt")

# ---- Logging ----
LOG_FILE = str(PROJECT_ROOT / "logs" / "errors.log")

# ---- Assets ----
LOGO_FILE = str(PROJECT_ROOT / "assets" / "TalentMiner_logo.png")

# ---- Matching ----
MATCH_THRESHOLD = int(os.getenv("MATCH_THRESHOLD", "85"))  # rapidfuzz partial_ratio cut-off

# ---- Database (Azure SQL) - set these in .env ----
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
DB_SERVER = os.getenv("DB_SERVER", "")
DB_NAME = os.getenv("DB_NAME", "ResumeDB")
DB_USER = os.getenv("DB_USER", "")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# Aliases kept for backward compatibility with v1 module imports
RESUME_FILE = PARSED_RESUMES_FILE
JOB_SKILL_FILE = PARSED_JD_FILE
