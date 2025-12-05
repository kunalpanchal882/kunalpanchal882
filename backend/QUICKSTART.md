# QUICK START GUIDE

## Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Google Gemini API key

## Step 1: Set Up Environment Variables

1. Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```

2. Get your Google Gemini API key:
   - Visit: https://aistudio.google.com/app/apikey
   - Click "Create API key in a new project"
   - Copy your API key

3. Edit `.env` and add your API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Run the Application

### Option A: Using the Quick Start Script (Recommended)
```bash
python quickstart.py
```
This will check your setup and start the server.

### Option B: Direct Start
```bash
uvicorn main:app --reload
```

## Step 4: Test the API

The API will be available at: **http://localhost:8000**

### Using the Interactive Docs:
1. Open: http://localhost:8000/docs
2. Find the **POST /parse** endpoint
3. Click **Try it out**
4. Upload a PDF or DOCX resume
5. Click **Execute**

### Using cURL:
```bash
curl -X POST http://localhost:8000/parse \
  -F "file=@resume.pdf"
```

### Using Python:
```bash
python test_api.py
```

## File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | FastAPI application and endpoints |
| `gemini_utile.py` | Google Gemini API integration |
| `utils.py` | File handling and text extraction |
| `requirements.txt` | Python dependencies |
| `.env` | API key configuration (create from .env.example) |
| `.env.example` | Template for environment variables |
| `README.md` | Full project documentation |
| `quickstart.py` | Automated setup and launch script |
| `test_api.py` | API testing script |

## Example Response

```json
{
  "name": "John Doe",
  "tech_stack": [
    "Python",
    "FastAPI",
    "Machine Learning",
    "PyTorch"
  ],
  "experience": 5.5,
  "fit_score": 8.5
}
```

## Troubleshooting

### Issue: "GEMINI_API_KEY not found"
- Ensure `.env` file exists in the project root
- Verify the API key is properly set in `.env`

### Issue: "Unsupported file type"
- Only PDF and DOCX files are supported
- Check file extension

### Issue: "Port 8000 already in use"
```bash
uvicorn main:app --reload --port 8001
```

### Issue: Module not found errors
```bash
pip install -r requirements.txt
```

## Project Structure

```
resume-screening/
├── main.py                 # FastAPI application
├── gemini_utile.py        # Gemini API utilities
├── utils.py               # File handling utilities
├── requirements.txt       # Dependencies
├── .env                   # API key (create this)
├── .env.example          # Template
├── .gitignore            # Git ignore rules
├── README.md             # Full documentation
├── QUICKSTART.md         # This file
├── quickstart.py         # Setup script
└── test_api.py          # API tests
```

## API Endpoints

### GET /
Returns API information

### POST /parse
Upload and parse a resume file
- Request: File (PDF or DOCX)
- Response: Structured resume data (JSON)

## Next Steps

1. **Read the full README.md** for comprehensive documentation
2. **Test with sample resumes** to ensure proper functionality
3. **Deploy to production** using Docker or cloud services
4. **Customize the Gemini prompt** in `gemini_utile.py` for your needs

## Support

- FastAPI Docs: https://fastapi.tiangolo.com
- Google Gemini API: https://ai.google.dev
- pdfplumber: https://github.com/jsvine/pdfplumber
- python-docx: https://python-docx.readthedocs.io

---

**Ready to go!** Start with `python quickstart.py` 🚀
