import streamlit as st
import re
st.set_page_config(
    page_title="Resume Keyword Extractor",
    page_icon="📄",
    layout="wide"
)
st.title("📄 Resume Keyword Extractor")
st.write("Upload a resume (.txt) file and extract important information.")
uploaded_file = st.file_uploader(
    "Upload Resume (.txt)",
    type=["txt"]
)
if uploaded_file is not None:
    resume = uploaded_file.read().decode("utf-8")
    email = re.findall(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        resume
    )
    phone = re.findall(
        r'(?:\+91[- ]?)?[6-9]\d{9}',
        resume
    )
    linkedin = re.findall(
        r'https?://(?:www\.)?linkedin\.com/\S+',
        resume
    )

    github = re.findall(
        r'https?://(?:www\.)?github\.com/\S+',
        resume
    )

    skills_list = [

        'python',
        'java',
        'c',
        'c++',
        'javascript',
        'html',
        'css',
        'sql',
        'mysql',
        'postgresql',
        'mongodb',
        'power bi',
        'excel',
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'tensorflow',
        'keras',
        'pytorch',
        'machine learning',
        'deep learning',
        'data science',
        'nlp',
        'computer vision',
        'aws',
        'azure',
        'gcp',
        'docker',
        'git',
        'linux'

    ]
    text = resume.lower()
    found_skills = []
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill.title())

    education = re.findall(
        r'BCA|MCA|B\.Tech|M\.Tech|Bachelor|Master|BSc|MSc|Diploma',
        resume,
        re.IGNORECASE
    )

    experience = re.findall(
        r'(\d+)\+?\s*(?:years?|yrs?)',
        resume,
        re.IGNORECASE
    )

    project_keywords = [

        "spam email detection",
        "movie recommendation system",
        "resume parser",
        "chatbot",
        "sentiment analysis",
        "house price prediction",
        "credit card fraud detection"

    ]
    projects = []

    for project in project_keywords:
        if project in text:
            projects.append(project.title())
    st.success("Resume Processed Successfully")

    st.markdown("---")
    st.subheader("📧 Email")
    st.write(email if email else "Not Found")

    st.subheader("📱 Phone")
    st.write(phone if phone else "Not Found")
    st.subheader("💼 LinkedIn")
    st.write(linkedin if linkedin else "Not Found")

    st.subheader("💻 GitHub")
    st.write(github if github else "Not Found")
    st.subheader("🛠 Skills")
    st.write(found_skills if found_skills else "Not Found")

    st.subheader("🎓 Education")

    st.write(education if education else "Not Found")
    st.subheader("💼 Experience")
    if experience:
        st.write(f"{experience[0]} Years")
    else:
        st.write("Not Found")
    st.subheader("📂 Projects")
    st.write(projects if projects else "Not Found")