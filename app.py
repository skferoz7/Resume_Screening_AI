from flask import Flask, render_template, request
import os
from resume_parser import extract_text
from model import analyze_resume

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files["resume"]
    job_desc = request.form["job_description"]

    path = os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(path)

    resume_text = extract_text(path)

    score, skills, missing = analyze_resume(resume_text, job_desc)

    print("DEBUG SCORE:", score, type(score))  # 👈 DEBUG LINE

    return render_template(
        "result.html",
        score=float(score),   # 👈 FORCE float
        skills=skills,
        missing=missing
    )

if __name__ == "__main__":
    app.run(debug=True)
