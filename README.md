📄 Resume Screening System
📌 Project Overview:

The Resume Screening System is a web-based application that helps automatically analyze resumes and match them with job descriptions.
It uses Natural Language Processing (NLP) techniques to calculate how well a resume matches a given job role, reducing manual screening time.

This project is useful for HR teams, recruiters, and students to quickly shortlist suitable candidates.

🎯 Objectives:

Automate resume screening process

Reduce manual effort and bias

Improve hiring efficiency

Provide a matching percentage between resume and job description

🛠️ Technologies Used:

Frontend: HTML, CSS, Bootstrap

Backend: Python, Flask

NLP: TF-IDF, Cosine Similarity

Tools: VS Code, GitHub

```
Resume-Screening/
│
├── app.py
├── model.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── result.html
│
├── static/
│   └── style.css
│
└── README.md
```
⚙️ Installation Steps
Step 1: Clone the Repository:
```
git clone https://github.com/skferoz7/Resume_Screening_AI.git
cd resume-screening_ai
```
Step 2: Create Virtual Environment (Optional):
```
python -m venv venv
venv\Scripts\activate
```
Step 3: Install Required Packages:
```
pip install -r requirements.txt
```

If requirements.txt is not available:

pip install flask scikit-learn nltk

▶️ How to Run the Project:
```
python app.py
```

Open browser and go to:

http://127.0.0.1:5000

🧠 How It Works (Step by Step):

User uploads or pastes resume text

User enters job description

Text is cleaned and processed

TF-IDF converts text into vectors

Cosine similarity calculates matching score

Result is displayed as percentage

📊 Features:

Resume & job description comparison

Skill extraction

Matching score generation

Simple and clean UI

Fast processing

🧪 Sample Use Case:

HR uploads multiple resumes

Enters job description

System highlights best-matched resumes

Shortlists candidates easily

📈 Future Enhancements:

PDF & DOCX resume upload

AI-based ranking system

Dashboard for recruiters

Multiple resume comparison

Cloud deployment

🧾 Sample Output:
```
Resume Match Score: 87%
Skills Matched: Python, Flask, SQL, Machine Learning
```
👨‍💻 Developed By

Shaik Feroz
B.Tech Computer Science
Hyderabad, Telangana

📜 License

This project is for educational purposes only.