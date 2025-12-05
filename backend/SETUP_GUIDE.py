#!/usr/bin/env python3
"""
Resume Parser API - Visual Setup Guide

This file generates a visual guide for setting up and using the Resume Parser API.
Run with: python SETUP_GUIDE.py
"""

def print_banner():
    banner = """
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║           RESUME PARSER API - COMPLETE FASTAPI APPLICATION                ║
║                                                                            ║
║     Parse resumes (PDF/DOCX) and extract structured data using            ║
║                      Google Gemini AI                                      ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def print_section(title, content):
    print(f"\n{'='*80}")
    print(f"  {title}")
    print(f"{'='*80}\n")
    print(content)

def print_installation_guide():
    guide = """
STEP 1: Get Google Gemini API Key
──────────────────────────────────
1. Visit: https://aistudio.google.com/app/apikey
2. Click "Create API key in a new project"
3. Copy your API key (starts with "AIza..." or similar)
4. Keep it safe - you'll need it in the next step

STEP 2: Create .env File
────────────────────────
1. In the project root, create a file named ".env"
2. Add this line (replace with your actual key):
   GEMINI_API_KEY=your_actual_api_key_here
3. Save the file

   Alternative: cp .env.example .env
   Then edit .env with your actual API key

STEP 3: Install Dependencies
─────────────────────────────
Run in terminal/command prompt:
   pip install -r requirements.txt

This will install:
  ✓ FastAPI         - Web framework
  ✓ Uvicorn         - Server
  ✓ pdfplumber      - PDF text extraction
  ✓ python-docx     - DOCX text extraction
  ✓ google-generativeai - Gemini API
  ✓ python-dotenv   - Environment variable management
  + dependencies of the above

STEP 4: Start the Application
──────────────────────────────
Option A (Recommended):
   python quickstart.py
   (This will check your setup and start the server)

Option B (Direct):
   uvicorn main:app --reload

You should see:
   INFO:     Uvicorn running on http://127.0.0.1:8000
   INFO:     Application startup complete
"""
    print(guide)

def print_testing_guide():
    guide = """
METHOD 1: Interactive Documentation (Best for Testing)
──────────────────────────────────────────────────────
1. Open in browser: http://localhost:8000/docs
2. Find "POST /parse" endpoint
3. Click "Try it out"
4. Select a PDF or DOCX file with your mouse
5. Click "Execute"
6. See the structured response!

METHOD 2: Using cURL (Terminal)
────────────────────────────────
# Upload a PDF resume:
curl -X POST http://localhost:8000/parse \\
  -F "file=@resume.pdf"

# Upload a DOCX resume:
curl -X POST http://localhost:8000/parse \\
  -F "file=@resume.docx"

METHOD 3: Using Python
──────────────────────
import requests

with open('resume.pdf', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/parse', files=files)

print(response.json())

METHOD 4: Automated Testing
────────────────────────────
python test_api.py
(This will run all tests and show results)
"""
    print(guide)

def print_file_structure():
    structure = """
PROJECT FILES OVERVIEW
══════════════════════

Core Application (3 files):
──────────────────────────
📄 main.py (143 lines)
   └─ FastAPI application & endpoints
   └─ POST /parse endpoint
   └─ Error handling
   └─ Response models

📄 gemini_utile.py (108 lines)
   └─ Google Gemini API integration
   └─ JSON parsing & validation
   └─ extract_resume_data() function

📄 utils.py (163 lines)
   └─ File handling utilities
   └─ PDF & DOCX text extraction
   └─ File validation & cleanup


Configuration Files:
───────────────────
⚙️  requirements.txt
   └─ All Python dependencies
   └─ Ready to: pip install -r requirements.txt

🔐 .env
   └─ Your Google Gemini API key
   └─ Should NOT be committed to git
   └─ Create by copying .env.example

📋 .env.example
   └─ Template for .env file
   └─ Safe to share (no secrets)


Documentation (3 comprehensive guides):
──────────────────────────────────────
📖 README.md
   └─ Complete project documentation
   └─ API endpoints explained
   └─ Usage examples
   └─ Troubleshooting guide

⚡ QUICKSTART.md
   └─ Quick setup guide
   └─ 4 simple steps to start

🔧 ADVANCED_CONFIG.md
   └─ Customization examples
   └─ Database integration
   └─ Docker deployment
   └─ Performance optimization


Helper Scripts:
──────────────
🚀 quickstart.py
   └─ Automated setup
   └─ Checks Python version
   └─ Validates .env file
   └─ Installs if needed
   └─ Starts the server

🧪 test_api.py
   └─ Tests all endpoints
   └─ Tests error handling
   └─ Provides test summary

📊 PROJECT_SUMMARY.py
   └─ Overview of all files
   └─ Feature list
   └─ Next steps


Git Configuration:
─────────────────
.gitignore
   └─ Excludes .env (API key safety)
   └─ Excludes __pycache__
   └─ Excludes virtual environment
"""
    print(structure)

def print_response_format():
    response = """
API RESPONSE FORMAT
═══════════════════

Successful Response (HTTP 200):
───────────────────────────────
{
  "name": "John Doe",
  "tech_stack": [
    "Python",
    "FastAPI",
    "Machine Learning",
    "PyTorch",
    "Scikit-learn",
    "Google Gemini API"
  ],
  "experience": 5.5,
  "fit_score": 8.5
}

Field Descriptions:
──────────────────
• name (string)
  The candidate's full name extracted from resume

• tech_stack (array of strings)
  Technologies, programming languages, and tools mentioned
  Examples: Python, Java, Docker, Kubernetes, React, etc.

• experience (number)
  Total years of professional experience
  Can be decimal (e.g., 5.5 for 5 years 6 months)

• fit_score (number 0-10)
  Skill match score based on Python + AI/ML expertise
  
  Score meaning:
  9-10  → Extensive Python and AI/ML expertise
  7-8   → Strong Python and AI/ML skills
  5-6   → Moderate Python with some AI/ML
  3-4   → Basic Python, limited AI/ML
  0-2   → Minimal or no Python/AI skills


Error Responses:
───────────────

400 Bad Request (Unsupported file):
{
  "detail": "Unsupported file type. Please upload a PDF or DOCX file."
}

500 Internal Server Error (Missing API key):
{
  "detail": "GEMINI_API_KEY not found in environment variables..."
}

500 Internal Server Error (Processing error):
{
  "detail": "An error occurred while processing the file: ..."
}
"""
    print(response)

def print_api_endpoints():
    endpoints = """
API ENDPOINTS REFERENCE
═══════════════════════

1. GET /
──────
Description:  Root endpoint - returns API information
URL:          http://localhost:8000/
Response:     API name, version, and available endpoints

Example cURL:
  curl http://localhost:8000/

Example Response:
  {
    "message": "Resume Parser API is running",
    "endpoints": {
      "parse": "POST /parse - Upload and parse a resume file"
    }
  }


2. POST /parse
──────────────
Description:  Upload and parse a resume file
URL:          http://localhost:8000/parse
Method:       POST
Content-Type: multipart/form-data (file upload)

Parameters:
  • file (required): PDF or DOCX resume file

Response:     Structured resume data (JSON)
Status Codes:
  • 200 OK - Successfully parsed
  • 400 Bad Request - Invalid file type or empty file
  • 500 Internal Server Error - API key missing or processing error

Example cURL:
  curl -X POST http://localhost:8000/parse \\
    -F "file=@resume.pdf"

Example Python:
  import requests
  
  with open('resume.pdf', 'rb') as f:
      files = {'file': f}
      response = requests.post(
          'http://localhost:8000/parse',
          files=files
      )
  
  print(response.json())
"""
    print(endpoints)

def print_troubleshooting():
    troubleshooting = """
TROUBLESHOOTING GUIDE
═════════════════════

Problem: "GEMINI_API_KEY not found"
──────────────────────────────────
Solution:
  1. Verify .env file exists in project root
  2. Verify the file contains: GEMINI_API_KEY=your_key
  3. Ensure it's not: GEMINI_API_KEY=your_gemini_api_key_here
  4. Check the key starts with "AIza..." or similar
  5. If unsure, get a new key from:
     https://aistudio.google.com/app/apikey


Problem: "Unsupported file type"
────────────────────────────────
Solution:
  Only PDF and DOCX files are supported
  • ✓ Supported: resume.pdf, resume.docx
  • ✗ Not supported: resume.txt, resume.jpg, resume.docm
  
  Tip: If you have a TXT or Word 97-2003 file, convert it to
       PDF or DOCX first (using Office or online converter)


Problem: Port 8000 already in use
─────────────────────────────────
Solution:
  Use a different port:
  
  uvicorn main:app --reload --port 8001
  
  Then access API at: http://localhost:8001


Problem: ModuleNotFoundError: No module named 'fastapi'
────────────────────────────────────────────────────────
Solution:
  Install dependencies:
  
  pip install -r requirements.txt
  
  Verify with:
  python -c "import fastapi; print(fastapi.__version__)"


Problem: Failed to extract text from file
──────────────────────────────────────────
Solution:
  The file may be corrupted or have special formatting
  
  Try:
  1. Open the file manually to verify it's readable
  2. Ensure it's a valid PDF/DOCX file
  3. Try converting to different format
  4. Check file size (very large files may cause issues)


Problem: Connection timeout or API is slow
───────────────────────────────────────────
Solution:
  Typical processing time: 3-10 seconds
  
  If slower:
  1. Check internet connection
  2. Verify Google Gemini API status:
     https://status.cloud.google.com
  3. Check API quota in Google Cloud Console
  4. Try again - sometimes API is busy


Problem: JSON parsing error from Gemini API
────────────────────────────────────────────
Solution:
  The API response format might have changed
  
  Try:
  1. Check if you're using the latest google-generativeai:
     pip install --upgrade google-generativeai
  2. Check the prompt in gemini_utile.py
  3. Verify API key is valid
  4. Try a different resume file


Problem: Virtual environment issues
───────────────────────────────────
Solution:
  Create a fresh virtual environment:
  
  Windows:
    python -m venv venv
    venv\\Scripts\\activate
    pip install -r requirements.txt
  
  macOS/Linux:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt


Can't find more help?
─────────────────────
Check these resources:
  • README.md - Comprehensive documentation
  • ADVANCED_CONFIG.md - Advanced usage
  • FastAPI docs: https://fastapi.tiangolo.com
  • Google Gemini API: https://ai.google.dev
  • pdfplumber: https://github.com/jsvine/pdfplumber
  • python-docx: https://python-docx.readthedocs.io
"""
    print(troubleshooting)

def print_summary():
    summary = """
PROJECT COMPLETION SUMMARY
═══════════════════════════

✓ Created 3 core application files:
  • main.py (FastAPI application)
  • gemini_utile.py (Gemini API integration)
  • utils.py (File handling & extraction)

✓ Created configuration files:
  • requirements.txt (Dependencies)
  • .env.example (API key template)
  • .gitignore (Git configuration)

✓ Created documentation:
  • README.md (Complete documentation)
  • QUICKSTART.md (Quick setup guide)
  • ADVANCED_CONFIG.md (Advanced customization)

✓ Created helper scripts:
  • quickstart.py (Automated setup)
  • test_api.py (API testing)
  • PROJECT_SUMMARY.py (File overview)
  • SETUP_GUIDE.py (This file)

✓ All code includes:
  • Comprehensive comments
  • Detailed docstrings
  • Error handling
  • Type hints
  • Production-ready quality

READY TO USE!
═════════════

Next steps:
  1. Get your API key: https://aistudio.google.com/app/apikey
  2. Create .env file: cp .env.example .env
  3. Add API key to .env
  4. Install dependencies: pip install -r requirements.txt
  5. Start server: python quickstart.py
  6. Test API: http://localhost:8000/docs

Questions? Check README.md or ADVANCED_CONFIG.md
Need help? See TROUBLESHOOTING section above
Ready to deploy? See ADVANCED_CONFIG.md for Docker setup

Happy coding! 🚀
"""
    print(summary)

def main():
    print_banner()
    
    print_section("INSTALLATION GUIDE", "Follow these steps to set up the project")
    print_installation_guide()
    
    print_section("TESTING GUIDE", "4 methods to test your API")
    print_testing_guide()
    
    print_section("FILE STRUCTURE", "Overview of all project files")
    print_file_structure()
    
    print_section("API ENDPOINTS", "Available endpoints and usage")
    print_api_endpoints()
    
    print_section("RESPONSE FORMAT", "Expected API responses")
    print_response_format()
    
    print_section("TROUBLESHOOTING", "Common issues and solutions")
    print_troubleshooting()
    
    print_section("SUMMARY", "Project completion status")
    print_summary()

if __name__ == "__main__":
    main()
