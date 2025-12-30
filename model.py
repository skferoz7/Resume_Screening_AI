import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- MASTER SKILL LIST ----------------
SKILLS = [
    "python", "java", "sql", "flask", "django",
    "html", "css", "javascript", "git", "linux",
    "machine learning", "data analysis", "aws",
    "c", "c++","data structures"
]

# ---------------- SKILL WEIGHTS (ATS STYLE) ----------------
SKILL_WEIGHTS = {
    "python": 3,
    "flask": 3,
    "django": 3,
    "sql": 2,
    "aws": 2,
    "java": 2,
    "javascript": 1,
    "html": 1,
    "css": 1,
    "git": 1,
    "linux": 1,
    "c": 1,
    "c++": 1,
    "machine learning": 2,
    "data analysis": 2,
    "data structure":2
}

# ---------------- CLEAN TEXT ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z+ ]", " ", text)
    return text

# ---------------- EXTRACT SKILLS ----------------
def extract_skills(text):
    text = text.lower()
    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return list(set(found))

# ---------------- MAIN ANALYSIS FUNCTION ----------------
def analyze_resume(resume_text, job_desc):
    # Clean input text
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_desc)

    # Extract skills
    resume_skills = extract_skills(resume_clean)
    job_skills = extract_skills(job_clean)

    # 🔥 Fallback: if job description has no skills
    if not job_skills:
        job_skills = SKILLS.copy()

    # Matched & Missing skills
    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    # ---------------- WEIGHTED SKILL SCORE ----------------
    total_weight = sum(SKILL_WEIGHTS.get(skill, 1) for skill in job_skills)
    matched_weight = sum(SKILL_WEIGHTS.get(skill, 1) for skill in matched_skills)

    skill_score = matched_weight / total_weight if total_weight else 0

    # ---------------- TEXT SIMILARITY (TF-IDF) ----------------
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_clean, job_clean])
    text_similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    # ---------------- FINAL SCORE ----------------
    final_score = (0.7 * skill_score) + (0.3 * text_similarity)
    match_percentage = round(final_score * 100, 2)

    # Cap unrealistic scores
    if match_percentage > 95:
        match_percentage = 95.0

    return {
        "match_percentage": match_percentage,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }
