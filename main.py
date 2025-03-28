import google.generativeai as genai
import PyPDF2 as pdf
import pdfplumber
import json
import re
def configure_genai(api_key):
    try:
        genai.configure(api_key=api_key) 
    except Exception as e:
        raise Exception(f"Failed to configure Generative AI: {str(e)}")
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)
        if not response or not response.text:
            raise Exception("Empty response received from Gemini")
        json_pattern = r'\{.*\}'
        match = re.search(json_pattern, response.text, re.DOTALL)
        if match:
            json_str = match.group()
            json_str = json_str.replace("\n", "").replace("\t", "").strip()
            try:
                response_json = json.loads(json_str) 
                required_fields = ["JD Match", "MissingKeywords", "Profile Summary"]
                for field in required_fields:
                    if field not in response_json:
                        raise ValueError(f"Missing required field: {field}")
                return json.dumps(response_json, indent=2)  # Return properly formatted JSON
            except json.JSONDecodeError as e:
                raise Exception(f"JSON parsing error: {str(e)}")
        else:
            raise Exception("Could not extract valid JSON response")
    except Exception as e:
        raise Exception(f"Error generating response: {str(e)}")
def extract_pdf_text(uploaded_file):
    try:
        text = []
        hyperlinks = []
        reader = pdf.PdfReader(uploaded_file)
        if len(reader.pages) == 0:
            raise Exception("PDF file is empty")
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text.strip())
        with pdfplumber.open(uploaded_file) as pdf_doc:
            for page in pdf_doc.pages:
                for annotation in page.annots or []:
                    if annotation.get("uri"):
                        hyperlinks.append(annotation["uri"])
        if not text:
            raise Exception("No text could be extracted from the PDF")
        extracted_content = "\n".join(text)
        if hyperlinks:
            extracted_content += "\n\nExtracted Hyperlinks:\n" + "\n".join(hyperlinks)
        return extracted_content
    except Exception as e:
        raise Exception(f"Error extracting PDF text: {str(e)}")
def prepare_prompt(resume_text, job_description):
    if not resume_text or not job_description:
        raise ValueError("Resume text and job description cannot be empty")
    prompt_template = """
    Act as an expert ATS (Applicant Tracking System) specialist with deep expertise in:
    - Technical fields
    - Software engineering
    - Data science
    - Data analysis
    - Big data engineering
    Evaluate the following resume against the job description. Consider that the job market 
    is highly competitive. Provide detailed feedback for resume improvement.
    Resume:
    {resume_text}
    Job Description:
    {job_description}
    Provide a response in the following JSON format ONLY:
    {{
        "JD Match": "percentage between 0-100",
        "MissingKeywords": ["keyword1", "keyword2", ...],
        "Profile Summary": "detailed analysis of the match and specific improvement suggestions"
    }}
    """
    return prompt_template.format(
        resume_text=resume_text.strip(),
        job_description=job_description.strip()
    )