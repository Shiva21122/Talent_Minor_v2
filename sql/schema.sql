-- TalentMiner database schema (Azure SQL / SQL Server)
-- Extracted from v1 main.py create_tables(). Statements separated by GO.

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
)
GO
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ParsedJobs' AND xtype='U')
CREATE TABLE ParsedJobs (
    reference_number VARCHAR(50),
    job_title NVARCHAR(255),
    weight FLOAT,
    skill NVARCHAR(MAX),
    timestamp DATETIME
)
GO
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
)
GO
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='JobReferenceSkills' AND xtype='U')
CREATE TABLE JobReferenceSkills (
    job_title NVARCHAR(255),
    keywords NVARCHAR(MAX),
    skills NVARCHAR(MAX)
)
GO
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Metadata' AND xtype='U')
CREATE TABLE Metadata (
    table_name NVARCHAR(100),
    last_updated DATETIME
)
GO
