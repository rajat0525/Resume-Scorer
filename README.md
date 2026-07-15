# Resume Parser & Completeness Scorer

A lightweight web application built with Python and Flask that allows users to upload a PDF resume, extracts the text, parses it into structured JSON using regex heuristics, and calculates a completeness score based on a predefined weighted template.

## 🚀 Features

- **PDF Text Extraction:** Seamlessly reads and extracts raw text from uploaded PDF files using `PyPDF2`.
- **Heuristic Parsing:** Uses Regular Expressions (Regex) to identify and extract key information like emails, phone numbers, education, experience, and skills into a structured JSON format.
- **Weighted Scoring System:** Compares the extracted data against a standard JSON template where different fields carry different weights (e.g., Experience = 25%, Email = 10%).
- **Clean User Interface:** A responsive, modern frontend built with HTML and CSS that clearly displays the overall score, matched/missing fields, and the raw JSON payload.
- **Separation of Concerns:** Organized cleanly into Backend (Python/Flask), Structure (HTML), and Styling (CSS).

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **PDF Processing:** PyPDF2
- **Frontend:** HTML5, CSS3, Jinja2 Templating
- **Text Processing:** Python `re` (Regular Expressions) module

## 📂 Project Structure

Ensure your files are organized exactly like this for the application to run properly:

```text
resume-scorer/                 <-- Your main project folder
│
├── app.py                     <-- Main Flask application and backend logic
├── README.md                  <-- Project documentation
│
├── static/                    <-- Folder for static assets (MUST be named "static")
│   └── style.css              <-- CSS styling for the frontend
│
└── templates/                 <-- Folder for HTML templates (MUST be named "templates")
    └── index.html             <-- Main user interface page
```

## ⚙️ Installation & Setup

Follow these steps to get the project running on your local machine.

**1. Clone or Create the Directory**
Create a folder for the project and navigate into it using your terminal.

```bash
mkdir resume-scorer
cd resume-scorer
```

**2. Set up a Virtual Environment (Recommended)**
This keeps your Python dependencies isolated from the rest of your system.

```bash
python -m venv venv
```

Activate the virtual environment:

- **Mac/Linux:** `source venv/bin/activate`
- **Windows:** `venv\Scripts\activate`

**3. Install the Required Libraries**
Install Flask and PyPDF2 using pip.

```bash
pip install Flask PyPDF2
```

**4. Run the Application**
Start the Flask development server.

```bash
python app.py
```

**5. View the App**
Open your web browser and navigate to:
`http://127.0.0.1:5000`

## 🖥️ Usage

1. Open the application in your web browser.
2. Click the **Choose File** (or Browse) button in the central upload area.
3. Select a `.pdf` resume from your computer.
4. Click **Upload Resume**.
5. The page will reload and display:
   - The overall completeness percentage score.
   - A breakdown of which weighted fields were successfully found.
   - A breakdown of which fields are missing.

## 🐛 Troubleshooting Common Errors

**HTTP 405: Method Not Allowed**
If you encounter this error when trying to upload a file, it means your server is blocking the form submission.

- **Fix 1 (Backend):** Ensure your Flask route in `app.py` explicitly allows POST requests: `@app.route('/', methods=['GET', 'POST'])`.
- **Fix 2 (Frontend):** Ensure your HTML form in `index.html` includes the method attribute: `<form method="POST" enctype="multipart/form-data">`.

## 🔮 Future Improvements

This is a functional prototype. For a production-grade enterprise application, the following improvements are recommended:

- **Advanced NLP Integration:** Replace the basic regex heuristics with a powerful Natural Language Processing library like `spaCy` or an LLM API for highly accurate entity extraction.
- **Database Support:** Add a database (e.g., PostgreSQL or SQLite) to store uploaded resumes and parsed JSON for later retrieval.
- **File Validation:** Add stricter security checks to ensure uploaded files are safe and are definitively PDFs before processing.
