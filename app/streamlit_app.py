"""TalentMiner Streamlit app (v1 Scripts/app.py, re-pathed).

Run from the project root:  streamlit run app/streamlit_app.py
"""
import streamlit as st
import pandas as pd
import pyodbc
from datetime import datetime
import os
import time
import sys
from pathlib import Path

# Make the src/ package importable when launched with `streamlit run app/streamlit_app.py`
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from talentminer.config.settings import LAST_UPDATE_FILE, LOGO_FILE
from talentminer.database.db import get_db_connection

st.set_page_config(layout="wide")



# ---------------- Database connection ----------------
try:
    conn = get_db_connection()
    st.success("Connected to database successfully.")
except Exception as e:
    st.error("Failed to connect to the database. Please check your Azure SQL Server settings and firewall rules.")
    st.stop()

# ---------------- Read last update ----------------
def read_last_update():
    try:
        mod_time = os.path.getmtime(LAST_UPDATE_FILE)
        with open(LAST_UPDATE_FILE, "r") as f:
            ts_str = f.read().strip()
        return ts_str, mod_time
    except:
        return "N/A", 0

# ---------------- Fetch options ----------------
def get_job_titles(conn):
    return pd.read_sql("SELECT DISTINCT target_job_title FROM ResumeMatches", conn)['target_job_title'].dropna().tolist()

def get_skills(conn):
    return pd.read_sql("SELECT DISTINCT skill FROM ParsedJobs", conn)['skill'].dropna().tolist()

# ---------------- Fetch matches ----------------
def fetch_matches_by_title(conn, title):
    query = """
    SELECT 
        name AS Name, 
        current_job_title AS [Current Title],
        email AS Email,
        phone AS Phone,
        ROUND(match_percent, 1) AS [Match %],
        matched_skills AS [Matched Skills],
        missing_skills AS [Missing Skills]
    FROM ResumeMatches
    WHERE target_job_title = ?
    ORDER BY match_percent DESC
    """
    df = pd.read_sql(query, conn, params=[title])
    df.index += 1
    return df

def fetch_matches_by_skills(conn, selected_skills):
    if not selected_skills:
        return pd.DataFrame()

    total = len(selected_skills)
    selected_set = set(skill.lower() for skill in selected_skills)
    resume_df = pd.read_sql("SELECT name, email, phone, job_title, skills FROM ParsedResumes", conn)

    results = []
    for _, row in resume_df.iterrows():
        resume_skills = set(s.strip().lower() for s in str(row['skills']).split(';'))
        matched = list(resume_skills & selected_set)
        missing = list(selected_set - resume_skills)
        percent = round((len(matched) / total) * 100, 1) if total > 0 else 0

        if percent >= 10:
            results.append({
                'Name': row['name'],
                'Current Title': row.get('job_title', ''),
                'Email': row['email'],
                'Phone': row['phone'],
                'Match %': percent,
                'Matched Skills': ", ".join(matched),
                'Missing Skills': ", ".join(missing)
            })

    df = pd.DataFrame(results)
    if not df.empty:
        df = df.sort_values(by="Match %", ascending=False)
        df.index += 1
    return df

# ---------------- Main Streamlit UI ----------------
def main():
    # Auto-refresh check
    ts_str, mod_time = read_last_update()
    if "last_mod_time" not in st.session_state:
        st.session_state.last_mod_time = mod_time
        st.session_state.last_ts_str = ts_str
    elif mod_time > st.session_state.last_mod_time:
        st.session_state.last_mod_time = mod_time
        st.session_state.last_ts_str = ts_str
        st.cache_data.clear()
        st.rerun()


    # Header
    st.image(LOGO_FILE, width=300)
    st.markdown("### **TalentMiner Resume Matcher**")
    st.markdown("*Parse. Match. Hire.*")
    st.caption(f"📅 Last updated: {st.session_state.last_ts_str}")

    conn = get_db_connection()
    option = st.radio("Search matched resumes by:", ["Job Title", "Skill"])

    with st.sidebar:
        st.subheader("🔎 Filter Options")
        match_range = st.slider("Select Match % Range", 0, 100, (0, 100))

    df = pd.DataFrame()

    if option == "Job Title":
        titles = get_job_titles(conn)
        selected_title = st.selectbox("Select Job Title", titles)
        if selected_title:
            df = fetch_matches_by_title(conn, selected_title)

    elif option == "Skill":
        skills = get_skills(conn)
        selected_skills = st.multiselect("Select Skills", skills)
        if selected_skills:
            df = fetch_matches_by_skills(conn, selected_skills)

    if not df.empty:
        df = df[(df["Match %"] >= match_range[0]) & (df["Match %"] <= match_range[1])]
        st.dataframe(df.style.format({"Match %": "{:.1f}"}), use_container_width=True)

        csv = df.reset_index(drop=True).to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Results as CSV", data=csv, file_name="matched_resumes.csv", mime='text/csv')

    conn.close()

if __name__ == "__main__":
    main()