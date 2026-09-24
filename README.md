# 📄 AI-Assisted Resume Screening & Job Match Analyzer

## 📌 Project Overview

The AI-Assisted Resume Screening & Job Match Analyzer is a web-based application that compares a candidate's resume with a given job description.

The system extracts text from a PDF resume, identifies predefined technical and soft skills, compares them with the skills required in the job description, and calculates a Job Match Score.

It also identifies missing skills and provides recommendations for skill development.

---

## 🎯 Objective

The main objectives of this project are:

- Automatically extract text from a resume PDF.
- Identify relevant skills from the resume.
- Identify required skills from a job description.
- Compare resume skills with job requirements.
- Calculate a skill-based Job Match Score.
- Identify missing skills.
- Provide skill-gap recommendations.
- Present the results through a simple web interface.

---

## ✨ Features

### 1. Resume Upload

The user can upload a resume in PDF format.

### 2. Resume Text Extraction

The application extracts readable text from the uploaded PDF.

### 3. Skill Detection

The system detects predefined technical and soft skills from the resume and job description.

### 4. Skill Matching

The application identifies skills that appear in both the resume and job description.

### 5. Job Match Score

The system calculates a skill-based compatibility score.

### Formula

**Job Match Score =**

**(Number of Matched Job Skills / Total Detected Job Skills) × 100**

### 6. Missing Skill Detection

The system identifies skills required by the job description but not detected in the resume.

### 7. Skill Gap Recommendations

The application recommends missing skills that the candidate can consider developing.

### 8. Interactive Interface

The application provides an interactive web interface using Streamlit.

---

## ⚙️ System Workflow

```text
Resume PDF
     ↓
PDF Text Extraction
     ↓
Resume Skill Detection
     ↓
Job Description
     ↓
Job Skill Detection
     ↓
Skill Comparison
     ↓
Matched & Missing Skills
     ↓
Job Match Score
     ↓
Skill Gap Recommendations


---

🛠️ Technologies Used

Python

Streamlit

PyPDF

Regular Expressions (Regex)

Natural Language Processing concepts

HTML/CSS styling through Streamlit



---

📂 Project Structure

ResumeAnalyzer/
│
├── app.py
├── app_backup.py
├── requirements.txt
├── README.md
└── venv/


---

🚀 How to Run the Project

Step 1: Open the project folder

Open the ResumeAnalyzer folder in Visual Studio Code.

Step 2: Activate the virtual environment

venv\Scripts\activate

Step 3: Install required packages

pip install -r requirements.txt

Step 4: Run the application

streamlit run app.py

Step 5: Open the application

The application will open in the web browser through a local Streamlit address.


---

📊 Example Output

The application displays:

Job Match Score

Number of matched skills

Number of missing skills

Matched skills

Missing skills

Recommended skills to develop

Skills detected in the resume

Skills detected in the job description



---

🔮 Future Scope

The project can be further improved by:

Using advanced NLP models for semantic skill matching.

Supporting more resume formats.

Expanding the skill database.

Using machine learning for improved job matching.

Adding multiple job-description comparison.

Adding resume improvement suggestions.

Providing downloadable analysis reports.

Adding a database for storing analysis history.



---

👩‍💻 Project Type

Software / NLP-based Application


---

📌 Disclaimer

The Job Match Score represents skill coverage based on the predefined skills detected by the application. It is not a prediction of hiring decisions or employment outcomes.