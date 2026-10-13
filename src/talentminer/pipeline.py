"""TalentMiner end-to-end pipeline (replaces v1 Scripts/main.py).

Usage (from the project root, after `pip install -e .`):
    python -m talentminer.pipeline            # parse + match + load to Azure SQL
    python -m talentminer.pipeline --no-db    # parse + match only (CSV outputs)
"""
import argparse
import os
from datetime import datetime

from talentminer.config import settings


def write_last_update_timestamp():
    with open(settings.LAST_UPDATE_FILE, "w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def main(load_db=True):
    os.makedirs(settings.PROCESSED_DIR, exist_ok=True)

    from talentminer.parsers.resume_parser import process_resumes
    from talentminer.parsers.job_parser import parse_jobs
    from talentminer.matching.matcher import match_all_resumes

    print("\n--- Starting Resume Parsing ---")
    process_resumes(strict=True)

    print("\n--- Starting Job Description Parsing ---")
    parse_jobs()

    print("\n--- Starting Resume-Job Matching ---")
    match_all_resumes()

    if load_db:
        print("\n--- Loading results to database ---")
        from talentminer.database.db import load_all_outputs
        load_all_outputs()
    else:
        print("\n--- Skipping database load (--no-db) ---")

    write_last_update_timestamp()
    print("\nDone.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the TalentMiner pipeline")
    parser.add_argument("--no-db", action="store_true", help="skip loading results into Azure SQL")
    args = parser.parse_args()
    main(load_db=not args.no_db)
