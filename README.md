📄 Smart ATS – AI-Powered Resume Analyzer

An intelligent ATS Resume Analyzer built using Flask, Google Gemini AI, PDF Parsing, and a modern,
animated UI.
It evaluates your resume against a job description and returns:

🔥 ATS Match Score

🔑 Missing Keywords

📝 Auto-Generated Profile Summary

📄 PDF Resume Parsing


🧠 How It Works

Upload your resume (PDF)

Paste the job description

The system extracts resume text

A custom ATS prompt is generated

Gemini AI analyzes your resume

You receive structured results including match score, missing keywords, and ATS-optimized insights

✨ Features

✔ AI-powered resume analysis

✔ Modern UI with gradients, Lottie animations & AOS effects

✔ Dark Mode toggle

✔ AJAX-based smooth interface (no page reloads)

✔ Clean Flask API structure

✔ Accurate PDF text extraction

✔ Visual match score bar & highlight badges

🧰 Tech Stack
Backend

Flask

Python

Google Generative AI (Gemini)

PyPDF2

python-dotenv

Frontend

Bootstrap 5

Custom CSS

AOS Animation

Lottie animations

JavaScript (Fetch API)

📁 Project Structure
ResumeAnalyzer/
│── flask_app.py
│── helper.py
│── requirements.txt
│── .env
│── README.md
│
├── templates/
│     └── index.html
│
└── static/
      ├── style.css
      └── main.js

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/ResumeAnalyzer.git
cd ResumeAnalyzer

2️⃣ Create a virtual environment
Windows
python -m venv venv
.\venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add your Gemini API key

Create a .env file in the root directory:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

▶️ Running the Application

Run the Flask server:

python flask_app.py


Then open:

👉 http://127.0.0.1:8501

or
👉 http://localhost:8501

🌐 Deploying the App (Render / Railway / VPS)
Install gunicorn
pip install gunicorn

Create a Procfile (for Heroku/Render)
web: gunicorn flask_app:app


Push to GitHub → Deploy to Render/Railway → Add GOOGLE_API_KEY to environment variables → Done.

🖼️ Screenshots (Add images later)
![Home Page](screenshots/home.png)
![Analysis Result](screenshots/result.png)

🔮 Future Enhancements

Export PDF report

Resume keyword optimization suggestions

Multi-resume comparison

User login and resume history

Integrated resume builder

🤝 Contributing

Contributions are welcome!
Please open an issue or submit a pull request.

⭐ Support

If you find this project useful, please ⭐ star the repository!

👨‍💻 Author

Shreyas Srivastava
