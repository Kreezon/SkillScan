import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import os
import json
from dotenv import load_dotenv
from main import configure_genai, get_gemini_response, extract_pdf_text, prepare_prompt
def initialize_session_state():
    if 'is_processing' not in st.session_state:
        st.session_state.is_processing = False
def run_app():
    load_dotenv()
    initialize_session_state()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("Please set the GOOGLE_API_KEY in your .env file")
        return
    try:
        configure_genai(api_key)
    except Exception as e:
        st.error(f"API configuration failed: {str(e)}")
        return
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #f0f4f8;  /* Light background color */
            color: #333;  /* Dark text color */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .sidebar h1 {
            color: #0072B1;  /* Custom color for title */
        }
        .sidebar h2 {
            color: #0056A1;  /* Custom color for subheader */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.sidebar:
        st.title("🎯SkillScan Smart ATS")
        st.subheader("Overview")
        st.write("""
        This application assists you in:
        - Evaluating the match between your resume and the job description
        - Identifying essential keywords that may be missing
        - Receiving tailored suggestions to enhance your resume
        """)

    st.title("📄 Resume Analyzer for ATS")
    st.subheader("Enhance Your Resume for Applicant Tracking Systems")
    
    job_description = st.text_area(
        "Job Description",
        placeholder="Paste the job description here...",
        help="Provide the complete job description for a thorough analysis"
    )
    
    resume_file = st.file_uploader(
        "Upload Your Resume (PDF)",
        type="pdf",
        help="Please upload your resume in PDF format"
    )
    
    if st.button("Analyze Resume", disabled=st.session_state.is_processing):
        if not job_description:
            st.warning("Please enter a job description.")
            return       
        if not resume_file:
            st.warning("Please upload a resume in PDF format.")
            return
        
        st.session_state.is_processing = True
        
        try:
            with st.spinner("📊 Analyzing your resume..."):
                resume_content = extract_pdf_text(resume_file)
                prompt_input = prepare_prompt(resume_content, job_description)
                analysis_response = get_gemini_response(prompt_input)
                analysis_data = json.loads(analysis_response)
                
                st.success("✨ Analysis Completed!")
                match_score = analysis_data.get("JD Match", "N/A")
                st.metric("Match Score", match_score)
                
                st.subheader("Missing Keywords")
                keywords_missing = analysis_data.get("MissingKeywords", [])
                if keywords_missing:
                    st.write(", ".join(keywords_missing))
                else:
                    st.write("All critical keywords are present!")
                
                st.subheader("Profile Summary")
                st.write(analysis_data.get("Profile Summary", "No summary available"))
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        
        finally:
            st.session_state.is_processing = False

if __name__ == "__main__":
    run_app()