import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Skill
SKILLS = {
    "python": ["python"],
    "java": ["java"],
    "sql": ["sql", "mysql", "postgresql"],
    "flask": ["flask"],
    "django": ["django"],
    "html": ["html"],
    "css": ["css"],
    "javascript": ["javascript", "js"],
    "git": ["git", "github"],
    "linux": ["linux", "unix"],
    "machine learning": ["machine learning", "ml"],
    "data analysis": ["data analysis", "data analytics"],
    "artificial intelligence": ["artificial intelligence", "ai"],
    "aws": ["aws", "amazon web services"],
    "c": ["c"],
    "c++": ["c++", "cpp"]
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", " ", text)
    return text

def extract_skills(text):
    text = text.lower()
    return list(set(skill for skill in SKILLS if skill in text))

def analyze_resume(resume_text, job_desc):
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_desc)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_clean, job_clean])

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    # 🔥 IMPORTANT: ensure numeric float
    score = round(float(similarity) * 100, 2)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    missing_skills = list(set(job_skills) - set(resume_skills))

    return score, resume_skills, missing_skills
