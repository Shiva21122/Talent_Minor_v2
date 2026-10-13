import os
import sys
import pyodbc
import pandas as pd
from datetime import datetime

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'project_root')))

# Import modules
from resume_parser import process_resumes
from job_parser import parse_jobs
from matcher import match_all_resumes
from settings import KEYWORDS_FILE

# Database connection
def get_db_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=resumedbserver1.database.windows.net;"
        "DATABASE=ResumeDB;"
        "UID=upad0024;"
        "PWD=Resumeproject@123;"
    )

# Create tables if not exist
def create_tables(cursor):
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ParsedResumes' AND xtype='U')
    CREATE TABLE ParsedResumes (
        resume_id VARCHAR(20),
        name NVARCHAR(255),
        email NVARCHAR(255),
        phone NVARCHAR(50),
        education NVARCHAR(MAX),
        job_title NVARCHAR(255),
        skills NVARCHAR(MAX),
        parsed_at DATETIME DEFAULT GETDATE()
    )""")

    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ParsedJobs' AND xtype='U')
    CREATE TABLE ParsedJobs (
        reference_number VARCHAR(50),
        job_title NVARCHAR(255),
        weight FLOAT,
        skill NVARCHAR(MAX),
        timestamp DATETIME
    )""")

    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ResumeMatches' AND xtype='U')
    CREATE TABLE ResumeMatches (
        resume_id VARCHAR(20),
        name NVARCHAR(255),
        email NVARCHAR(255),
        phone NVARCHAR(50),
        current_job_title NVARCHAR(255),
        reference_number VARCHAR(50),
        target_job_title NVARCHAR(255),
        match_percent FLOAT,
        matched_skills NVARCHAR(MAX),
        missing_skills NVARCHAR(MAX),
        matched_at DATETIME DEFAULT GETDATE()
    )""")

    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='JobReferenceSkills' AND xtype='U')
    CREATE TABLE JobReferenceSkills (
        job_title NVARCHAR(255),
        keywords NVARCHAR(MAX),
        skills NVARCHAR(MAX)
    )""")

    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Metadata' AND xtype='U')
    CREATE TABLE Metadata (
        table_name NVARCHAR(100),
        last_updated DATETIME
    )""")

    cursor.connection.commit()

# Delete existing data before inserting
def clear_table(cursor, table_name):
    cursor.execute(f"DELETE FROM {table_name}")
    cursor.connection.commit()

# Load CSV into a table
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

    # Update timestamp in Metadata table
    cursor.execute("""
        MERGE Metadata AS target
        USING (SELECT ? AS table_name, ? AS last_updated) AS source
        ON target.table_name = source.table_name
        WHEN MATCHED THEN UPDATE SET last_updated = source.last_updated
        WHEN NOT MATCHED THEN INSERT (table_name, last_updated) VALUES (source.table_name, source.last_updated);
    """, table_name, datetime.now())
    cursor.connection.commit()

# Write update time for app refresh trigger

def main():
    print("\n--- Starting Resume Parsing ---")
    process_resumes(strict=True)

    print("\n--- Starting Job Description Parsing ---")
    parse_jobs()

    print("\n--- Starting Resume-Job Matching ---")
    match_all_resumes()

    print("\n--- Connecting to Database ---")
    conn = get_db_connection()
    cursor = conn.cursor()
    create_tables(cursor)

    insert_csv_to_db("output/parsed_resumes.csv", "ParsedResumes", cursor)
    insert_csv_to_db("output/parsed_job_skills.csv", "ParsedJobs", cursor)
    insert_csv_to_db("output/resume_match_results.csv", "ResumeMatches", cursor)
    insert_csv_to_db(KEYWORDS_FILE, "JobReferenceSkills", cursor)
    
    with open("last_update.txt", "w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    conn.close()
    
def write_last_update_timestamp():
    with open("last_update.txt", "w") as f:
        f.write(datetime.now().isoformat())

if __name__ == "__main__":
    main()