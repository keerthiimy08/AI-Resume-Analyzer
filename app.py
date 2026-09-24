import streamlit as st
from pypdf import PdfReader
import re

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>

.main-title {
    font-size: 38px;
    font-weight: bold;
    text-align: center;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666666;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Title
# -----------------------------
st.markdown(
    '<div class="main-title">📄 AI-Assisted Resume Screening & Job Match Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze resume skills and compare them with job requirements</div>',
    unsafe_allow_html=True
)

st.divider()


# -----------------------------
# Skill Database
# -----------------------------
skills = [
    "python",
    "java",
    "c++",
    "c",
    "javascript",
    "html",
    "css",
    "sql",
    "mysql",
    "mongodb",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "streamlit",
    "git",
    "github",
    "react",
    "node.js",
    "computer vision",
    "nlp",
    "natural language processing",
    "communication",
    "problem solving",
    "cloud",
    "aws",
    "azure"
]


# -----------------------------
# PDF Text Extraction
# -----------------------------
def extract_text_from_pdf(uploaded_file):

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# -----------------------------
# Skill Extraction
# -----------------------------
def find_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills:

        # Escape special characters
        escaped_skill = re.escape(skill)

        # Match the skill as a complete word or phrase
        pattern = r"(?<!\w)" + escaped_skill + r"(?!\w)"

        if re.search(pattern, text):

            found_skills.append(skill)

    return sorted(set(found_skills))


# -----------------------------
# Input Section
# -----------------------------
st.subheader("📥 Enter Your Information")

col1, col2 = st.columns(2)

with col1:

    st.write("### 📄 Upload Resume")

    uploaded_file = st.file_uploader(
        "Upload your resume in PDF format",
        type=["pdf"]
    )

with col2:

    st.write("### 💼 Job Description")

    job_description = st.text_area(
        "Paste the job description here",
        height=250,
        placeholder="Paste the job description here..."
    )


st.divider()


# -----------------------------
# Analyze Button
# -----------------------------
if st.button(
    "🔍 Analyze Resume",
    type="primary",
    use_container_width=True
):

    if uploaded_file is None:

        st.warning("Please upload a resume PDF.")

    elif not job_description.strip():

        st.warning("Please paste a job description.")

    else:

        # -----------------------------
        # Extract Resume Text
        # -----------------------------
        resume_text = extract_text_from_pdf(
            uploaded_file
        )

        # -----------------------------
        # Display Extracted Resume Text
        # -----------------------------
        st.subheader("📄 Extracted Resume Text")

        with st.expander("View extracted resume text"):

            st.text(resume_text)

        # -----------------------------
        # Check Resume Text
        # -----------------------------
        if not resume_text.strip():

            st.error(
                "Could not extract text from this PDF. "
                "Please upload a text-based PDF."
            )

        else:

            # -----------------------------
            # Find Skills
            # -----------------------------
            resume_skills = find_skills(
                resume_text
            )

            job_skills = find_skills(
                job_description
            )

            # -----------------------------
            # Matched Skills
            # -----------------------------
            matched_skills = sorted(
                set(resume_skills) &
                set(job_skills)
            )

            # -----------------------------
            # Missing Skills
            # -----------------------------
            missing_skills = sorted(
                set(job_skills) -
                set(resume_skills)
            )

            # -----------------------------
            # Calculate Match Score
            # -----------------------------
            if job_skills:

                match_score = round(
                    (
                        len(matched_skills)
                        /
                        len(job_skills)
                    ) * 100,
                    2
                )

            else:

                match_score = 0


            # -----------------------------
            # Analysis Results
            # -----------------------------
            st.subheader("📊 Analysis Results")

            score_col, matched_col, missing_col = st.columns(3)

            with score_col:

                st.metric(
                    "🎯 Job Match Score",
                    f"{match_score}%"
                )

            with matched_col:

                st.metric(
                    "✅ Matched Skills",
                    len(matched_skills)
                )

            with missing_col:

                st.metric(
                    "⚠️ Missing Skills",
                    len(missing_skills)
                )


            # -----------------------------
            # Match Progress
            # -----------------------------
            st.write("### Match Strength")

            st.progress(
                match_score / 100
            )


            # -----------------------------
            # Score Interpretation
            # -----------------------------
            if match_score >= 80:

                st.success(
                    "🟢 Strong skill match with the job description."
                )

            elif match_score >= 60:

                st.info(
                    "🟡 Moderate skill match. "
                    "Some additional skills may be required."
                )

            else:

                st.warning(
                    "🔴 Low skill match. "
                    "Consider developing the missing skills."
                )


            st.divider()


            # -----------------------------
            # Matched Skills
            # -----------------------------
            st.subheader("✅ Matched Skills")

            if matched_skills:

                st.write(
                    ", ".join(
                        skill.title()
                        for skill in matched_skills
                    )
                )

            else:

                st.write(
                    "No matching skills detected."
                )


            # -----------------------------
            # Missing Skills
            # -----------------------------
            st.subheader("⚠️ Missing Skills")

            if missing_skills:

                st.write(
                    ", ".join(
                        skill.title()
                        for skill in missing_skills
                    )
                )

            else:

                st.write(
                    "No missing skills detected."
                )


            # -----------------------------
            # Skill Gap Recommendations
            # -----------------------------
            st.subheader(
                "🎯 Recommended Skills to Develop"
            )

            if missing_skills:

                st.write(
                    "Consider improving the following skills "
                    "to better match the job requirements:"
                )

                for skill in missing_skills:

                    st.write(
                        f"• {skill.title()}"
                    )

            else:

                st.success(
                    "Your resume covers all detected skills "
                    "in the job description!"
                )


            st.divider()


            # -----------------------------
            # Skills Detected in Resume
            # -----------------------------
            st.subheader(
                "📌 Skills Detected in Resume"
            )

            if resume_skills:

                st.write(
                    ", ".join(
                        skill.title()
                        for skill in resume_skills
                    )
                )

            else:

                st.write(
                    "No predefined skills detected."
                )


            # -----------------------------
            # Skills Detected in Job Description
            # -----------------------------
            st.subheader(
                "🎯 Skills Detected in Job Description"
            )

            if job_skills:

                st.write(
                    ", ".join(
                        skill.title()
                        for skill in job_skills
                    )
                )

            else:

                st.write(
                    "No predefined skills detected."
                )


            # -----------------------------
            # Completion Message
            # -----------------------------
            st.divider()

            st.success(
                "✅ Analysis completed successfully!"
            )


# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "NLP-based resume screening system using "
    "automated skill extraction and skill matching."
)