from flask import Flask, render_template, request, jsonify
import PyPDF2
import re
import os

app = Flask(__name__)

# Standard JSON Template with weighted fields (Total = 100)
TEMPLATE_WEIGHTS = {
    "name": 15,
    "email": 10,
    "phone": 10,
    "education": 20,
    "experience": 25,
    "skills": 20
}

def extract_text_from_pdf(file_stream):
    """Extracts raw text from an uploaded PDF file."""
    text = ""
    try:
        reader = PyPDF2.PdfReader(file_stream)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def parse_resume_to_json(text):
    """
    Simulates parsing a resume into JSON using basic heuristics.
    For a production backend environment, you would replace this with 
    a robust NLP pipeline (e.g., spaCy) or an LLM API.
    """
    parsed_data = {}
    text_lower = text.lower()

    # 1. Email Extraction
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    if email_match:
        parsed_data["email"] = email_match.group(0)

    # 2. Phone Extraction (Basic international format)
    phone_match = re.search(r'\(?\+?[0-9]{1,3}\)?[\s.-]?[0-9]{3}[\s.-]?[0-9]{3,4}', text)
    if phone_match:
        parsed_data["phone"] = phone_match.group(0)

    # 3. Education Section
    if re.search(r'\b(education|university|college|degree|bachelor|master)\b', text_lower):
        parsed_data["education"] = "Education details found."

    # 4. Experience Section
    if re.search(r'\b(experience|employment|work history|career)\b', text_lower):
        parsed_data["experience"] = "Experience details found."

    # 5. Skills Section
    if re.search(r'\b(skills|technologies|tools|languages)\b', text_lower):
        parsed_data["skills"] = "Skills details found."

    # 6. Name (Heuristic: Assuming a name exists if the resume has sufficient text)
    if len(text) > 100:
        parsed_data["name"] = "Name assumed present."

    return parsed_data

def calculate_completeness(parsed_json):
    """Compares the parsed JSON against the standard template weights."""
    score = 0
    matched_fields = []
    missing_fields = []

    for field, weight in TEMPLATE_WEIGHTS.items():
        if field in parsed_json and parsed_json[field]:
            score += weight
            matched_fields.append(field)
        else:
            missing_fields.append(field)

    return {
        "percentage": score,
        "matched": matched_fields,
        "missing": missing_fields,
        "extracted_json": parsed_json
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        if 'resume' not in request.files:
            return "No file uploaded", 400
        
        file = request.files['resume']
        if file.filename == '':
            return "No selected file", 400
            
        if file and file.filename.endswith('.pdf'):
            # 1. Extract Text
            raw_text = extract_text_from_pdf(file)
            
            # 2. Parse to JSON
            parsed_json = parse_resume_to_json(raw_text)
            
            # 3. Calculate Score
            result = calculate_completeness(parsed_json)
            
    return render_template('index.html', result=result, template_weights=TEMPLATE_WEIGHTS)

if __name__ == '__main__':
    app.run(debug=True)