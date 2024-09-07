from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
import PyPDF2

genai.configure(api_key=os.environ["GOOGLE_API_KEY"]) # setting up the API key

def get_response(input,pdf_content,prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")   # defining model
    response = model.generate_content([input, pdf_content, prompt])  # giving input, pdf content and prompt to the model
    return response.text


def extract_text_from_pdf(pdf_file): # Function to extract text from PDF
    if pdf_file is not None:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        return text
    else:
        raise FileNotFoundError("File not uploaded")

# Function to load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#  Building streamlit app UI
st.set_page_config(page_title="ATS Resume Tracker", page_icon="📄")
load_css('styles.css')
st.markdown('<div class="custom-mainheader">ATS Resume Tracker 📄</div>', unsafe_allow_html=True)
input_Job_Description = st.text_area("Job Description", key="input")
uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf"], key="file")

if uploaded_file is not None:
    st.write("Resume Uploaded Successfully")


input_prompt1 = """You are an experienced Human Resource Manager. Your task is to review the provided resume 
against the provided job description. Please share your prodessional feedback on the resume whether the candidate's profile
matches the job description or not. Please provide the highlights on strengths and weakness of the applicant in relation 
to the specified job description."""

input_prompt2 = """You are a technical human resource manager. Your role is to scrutinize the resume of the candidate
in light of the provided job description. share your insights on suitability of applicant for the role from HR perspective.
Additionally offer advice on enhancing the candidate's skills and identify the areas of improvement."""


input_prompt3 ="""You are an ATS (Applicant Tracking System) scanner with deep understanding of ATS fucntionality.
your task is to evaluate the resume against the provided job description. Identify the missing keywords in the resume.
You have to suggest the missing keywords in the resume that would align with the job description."""


input_prompt4 = """You are an ATS (Applicant Tracking System) scanner with deep understanding of ATS fucntionality.
your task is to evaluate the resume against the provided job description. Give the percentage match of resume with job description
if the resume matches the job description. Add your reasons in the end that why the resume match percentage is low or high."""

# Arranging the buttons in a 2x2 grid format
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    submit1 = st.button("Tell Me about my Resume")
with col2:
    submit2 = st.button("How can I improve my skills?")
with col3:
    submit3 = st.button("Suggest Missing keywords")
with col4:
    submit4 = st.button("Percentage Match of my Resume")


if submit1:
    if uploaded_file is not None:
        pdf_content = extract_text_from_pdf(uploaded_file)
        response = get_response(input_prompt1,pdf_content,input_Job_Description)
        st.write(response)
    else:
        st.write("Please upload the Resume.")
elif submit2:
    if uploaded_file is not None:
        pdf_content = extract_text_from_pdf(uploaded_file)
        response = get_response(input_prompt2,pdf_content,input_Job_Description)
        st.write(response)
    else:
        st.write("Please upload the Resume.")
elif submit3:
    if uploaded_file is not None:
        pdf_content = extract_text_from_pdf(uploaded_file)
        response = get_response(input_prompt3,pdf_content,input_Job_Description)
        st.write(response)
    else:
        st.write("Please upload the Resume.")
elif submit4:
    if uploaded_file is not None:
        pdf_content = extract_text_from_pdf(uploaded_file)
        response = get_response(input_prompt4,pdf_content,input_Job_Description)
        st.write(response)
    else:
        st.write("Please upload the Resume.")