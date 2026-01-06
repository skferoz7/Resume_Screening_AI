from flask import Flask, render_template, request
import os
import sqlite3
from resume_parser import extract_text
from model import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

DB_NAME = "database.db"

# ---------------- DB CONNECTION ----------------
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- ROUTES ----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files["resume"]
    job_desc = request.form["job_description"]

    # Save resume file
    path = os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(path)

    # Extract resume text
    resume_text = extract_text(path)

    # ---------- AI ANALYSIS (FIXED) ----------
    result = analyze_resume(resume_text, job_desc)

    score = result["match_percentage"]
    skills = result["matched_skills"]
    missing = result["missing_skills"]

    # ❌ DO NOT convert again
    # score = float(score)  <-- REMOVE THIS LINE

    # ---------- SAVE TO DATABASE ----------
    conn = get_db_connection()
    conn.execute(
        """
        INSERT INTO screening_results (job_description, match_score)
        VALUES (?, ?)
        """,
        (job_desc, score)
    )
    conn.commit()
    conn.close()

    # ---------- SHOW RESULT ----------
    return render_template(
        "result.html",
        score=score,
        skills=skills,
        missing=missing
    )


if __name__ == "__main__":
    app.run()
