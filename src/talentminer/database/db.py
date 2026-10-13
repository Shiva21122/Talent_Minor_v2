"""Azure SQL access: connection, schema creation and CSV loading.

Moved out of v1 main.py. Logic is unchanged except that credentials are read
from environment variables instead of being hardcoded.
"""
import os
from datetime import datetime

import pandas as pd

from talentminer.config import settings


def get_db_connection():
    import pyodbc  # imported lazily so the pipeline can run without ODBC installed

    if not (settings.DB_SERVER and settings.DB_USER and settings.DB_PASSWORD):
        raise RuntimeError(
            "Database settings missing. Copy .env.example to .env and fill in "
            "DB_SERVER, DB_NAME, DB_USER and DB_PASSWORD."
        )
    return pyodbc.connect(
        f"DRIVER={{{settings.DB_DRIVER}}};"
        f"SERVER={settings.DB_SERVER};"
        f"DATABASE={settings.DB_NAME};"
        f"UID={settings.DB_USER};"
        f"PWD={settings.DB_PASSWORD};"
    )


def create_tables(cursor):
    """Create tables if they don't exist. Same DDL as sql/schema.sql."""
    schema_path = settings.PROJECT_ROOT / "sql" / "schema.sql"
    for statement in schema_path.read_text(encoding="utf-8").split("\nGO\n"):
        if statement.strip():
            cursor.execute(statement)
    cursor.connection.commit()


def clear_table(cursor, table_name):
    cursor.execute(f"DELETE FROM {table_name}")
    cursor.connection.commit()


def insert_csv_to_db(csv_path, table_name, cursor):
    if not os.path.exists(csv_path):
        print(f" File not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    print(f" Inserting data from {csv_path} into {table_name}...")

    clear_table(cursor, table_name)

    for _, row in df.iterrows():
        if table_name == "ParsedResumes":
            cursor.execute(f"""
                INSERT INTO {table_name} (resume_id, name, email, phone, education, job_title, skills)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            str(row.get('resume_id', '')),
            str(row.get('Name', '')),
            str(row.get('Email', '')),
            str(row.get('Phone', '')),
            str(row.get('Education', '')),
            str(row.get('Job Title', '')),
            str(row.get('Skills', '')))

        elif table_name == "ParsedJobs":
            weight = pd.to_numeric(row.get('weight', 0), errors='coerce')
            timestamp = pd.to_datetime(row.get('timestamp', None), errors='coerce')
            cursor.execute(f"""
                INSERT INTO {table_name} (reference_number, job_title, weight, skill, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """,
            str(row.get('reference_number', '')),
            str(row.get('job_title', '')),
            weight if pd.notnull(weight) else 0.0,
            str(row.get('skill', '')),
            timestamp if pd.notnull(timestamp) else None)

        elif table_name == "ResumeMatches":
            match_percent = pd.to_numeric(row.get('match_percent', 0), errors='coerce')
            cursor.execute(f"""
                INSERT INTO {table_name} (
                    resume_id, name, email, phone, current_job_title, reference_number,
                    target_job_title, match_percent, matched_skills, missing_skills
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            str(row.get('resume_id', '')),
            str(row.get('name', '')),
            str(row.get('email', '')),
            str(row.get('phone', '')),
            str(row.get('current_job_title', '')),
            str(row.get('reference_number', '')),
            str(row.get('target_job_title', '')),
            match_percent if pd.notnull(match_percent) else 0.0,
            str(row.get('matched_skills', '')),
            str(row.get('missing_skills', '')))

        elif table_name == "JobReferenceSkills":
            cursor.execute(f"""
                INSERT INTO {table_name} (job_title, keywords, skills)
                VALUES (?, ?, ?)
            """,
            str(row.get('Job Title', '')),
            str(row.get('Keywords', '')),
            str(row.get('Skills', '')))

    cursor.connection.commit()
    print(f" Inserted {len(df)} rows into {table_name}.")

    cursor.execute("""
        MERGE Metadata AS target
        USING (SELECT ? AS table_name, ? AS last_updated) AS source
        ON target.table_name = source.table_name
        WHEN MATCHED THEN UPDATE SET last_updated = source.last_updated
        WHEN NOT MATCHED THEN INSERT (table_name, last_updated) VALUES (source.table_name, source.last_updated);
    """, table_name, datetime.now())
    cursor.connection.commit()


def load_all_outputs():
    conn = get_db_connection()
    cursor = conn.cursor()
    create_tables(cursor)
    insert_csv_to_db(settings.PARSED_RESUMES_FILE, "ParsedResumes", cursor)
    insert_csv_to_db(settings.PARSED_JD_FILE, "ParsedJobs", cursor)
    insert_csv_to_db(settings.MATCH_RESULTS_FILE, "ResumeMatches", cursor)
    insert_csv_to_db(settings.KEYWORDS_FILE, "JobReferenceSkills", cursor)
    conn.close()
