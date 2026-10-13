import csv
import re
from fuzzywuzzy import fuzz
import os


REFERENCE_CSV = os.path.join(os.path.dirname(__file__), "Health_Canada_Jobs_With_Skills_1.csv")

def get_all_job_titles():
    job_titles = set()
    try:
        with open(REFERENCE_CSV, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                job = row.get('Job Title', '').strip()
                if job:
                    job_titles.add(job)
        return list(job_titles)
    except Exception as e:
        print(f"Error reading job titles from CSV: {e}")
        return []
def extract_skills_from_resume(resume_text, job_title):
    resume_text = resume_text.lower()
    matched_skills = []
    fallback_skills = []

    def split_skills(skill_str):
   
        parts = re.split(r",| or | and |/|\\|;", skill_str, flags=re.IGNORECASE)
        cleaned = []
        for part in parts:
            part = part.strip().lower()
     
            part = re.sub(r"^(proficient in|experienced with|experience in|strong|good knowledge of|familiarity with|bachelor's in|master's in|related field|skills in|including)\s*", "", part)
            if part and len(part) > 1 and not part.startswith("("):
                cleaned.append(part)
        return cleaned

    try:
        with open(REFERENCE_CSV, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                job = row.get('Job Title', '').strip()
                skills_str = row.get('Skills', '').strip()
                if not job or not skills_str:
                    continue
                similarity = fuzz.token_sort_ratio(job.lower(), job_title.lower())
                skills = split_skills(skills_str)
                found = []
                for sk in skills:
                    if re.search(rf'\b{re.escape(sk)}\b', resume_text):
                        found.append(sk)
                    elif sk in resume_text:
                        found.append(sk)
                if similarity >= 70:
                    matched_skills.extend(found)
                elif not matched_skills:
                    fallback_skills.extend(found)
        if matched_skills:
            return list(set(matched_skills))
        elif fallback_skills:
            return list(set(fallback_skills))
        else:
            return []
    except Exception as e:
        print(f"Error matching skills: {e}")
        return []
def get_reference_csv_path():
  
    return REFERENCE_CSV