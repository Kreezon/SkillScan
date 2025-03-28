# SkillScan Smart ATS

## Overview
SkillScan Smart ATS is a Streamlit-based web application designed to enhance your resume for Applicant Tracking Systems (ATS). It evaluates the compatibility of your resume with job descriptions, identifies missing keywords, and provides tailored suggestions for improvement.

## Features
- **Resume Analysis**: Evaluates how well your resume matches a given job description.
- **Keyword Identification**: Highlights missing essential keywords.
- **Profile Summary**: Offers specific improvement suggestions.

## Installation

### Prerequisites
- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [pdfplumber](https://pypi.org/project/pdfplumber/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/kreezon/skillscan-smart-ats.git
   ```
2. Navigate to the project directory:
   ```bash
   cd skillscan-smart-ats
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Create a `.env` file in the project root directory and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key
```

## Usage
Run the Streamlit application using the following command:

```bash
streamlit run app.py
```

## How It Works
1. Upload your resume in PDF format.
2. Paste the job description in the provided text area.
3. Click the "Analyze Resume" button.
4. View the match score, missing keywords, and profile summary.

## File Structure
```
project-root/
├── app.py
├── main.py
├── .env
├── requirements.txt
├── README.md
```

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
