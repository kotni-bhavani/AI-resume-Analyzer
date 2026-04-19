import streamlit as st
import PyPDF2

# Predefined skills list
skills_list = [
    "python", "java", "c++", "machine learning", "data science",
    "sql", "html", "css", "javascript", "cloud computing",
    "deep learning", "ai", "communication", "problem solving"
]

# Extract text from PDF
def extract_text(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text.lower()

# Analyze resume
def analyze_resume(resume_text):
    found_skills = []
    for skill in skills_list:
        if skill in resume_text:
            found_skills.append(skill)

    score = (len(found_skills) / len(skills_list)) * 100
    return found_skills, score

# Suggestions
def get_missing_skills(found_skills):
    return list(set(skills_list) - set(found_skills))[:5]

# UI
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get instant analysis")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    try:
        resume_text = extract_text(uploaded_file)

        if resume_text.strip() == "":
            st.error("❌ Could not extract text. Upload a proper text-based PDF.")
        else:
            found_skills, score = analyze_resume(resume_text)
            missing_skills = get_missing_skills(found_skills)

            st.success("✅ Analysis Completed")

            st.subheader("📊 Resume Score")
            st.write(f"{score:.2f}%")

            st.subheader("✅ Skills Found")
            st.write(found_skills if found_skills else "No skills detected")

            st.subheader("⚠️ Missing Skills (Suggestions)")
            st.write(missing_skills)

    except Exception as e:
        st.error(f"Error: {e}")