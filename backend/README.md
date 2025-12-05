# Resume Parser API

A FastAPI-based REST API that parses resume files (PDF/DOCX) and extracts structured data using Google Gemini API.

## Features

- **File Upload**: Accept PDF and DOCX resume files via `/parse` endpoint
- **Text Extraction**: Automatically extracts text from uploaded files
- **AI-Powered Parsing**: Uses Google Gemini API to extract structured resume data
- **Structured Response**: Returns JSON with candidate name, tech stack, experience, and skill-based fit score
- **Error Handling**: Comprehensive error handling for missing API keys, unsupported files, and processing errors
- **Temporary File Cleanup**: Automatically deletes uploaded files after processing

## Project Structure

```
resume-screening/
├── main.py                 # FastAPI application and endpoints
├── gemini_utile.py        # Google Gemini API integration
├── utils.py               # File handling and text extraction utilities
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
└── README.md             # This file
```

## Installation

### 1. Clone or Download the Project

```bash
cd resume-screening
```

### 2. Create a Virtual Environment (Optional but Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

1. Get your Google Gemini API key:
   - Visit: https://aistudio.google.com/app/apikey
   - Click "Create API key"
   - Copy the API key

2. Create a `.env` file in the project root:

```bash
cp .env.example .env
```

3. Edit `.env` and add your API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

## Running the Application

### Option 1: Using Uvicorn (Recommended)

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

### Option 2: Run Directly

```bash
python main.py
```

## API Endpoints

### 1. Root Endpoint

**GET** `/`

Returns API information and available endpoints.

**Example Response:**
```json
{
  "message": "Resume Parser API is running",
  "endpoints": {
    "parse": "POST /parse - Upload and parse a resume file"
  }
}
```

### 2. Parse Resume Endpoint

**POST** `/parse`

Uploads and parses a resume file.

**Request:**
- **File**: PDF or DOCX file (form-data)

**Success Response (200 OK):**
```json
{
  "name": "John Doe",
  "tech_stack": [
    "Python",
    "FastAPI",
    "Google Gemini API",
    "Machine Learning",
    "PyTorch",
    "Scikit-learn"
  ],
  "experience": 5.5,
  "fit_score": 8.5
}
```

**Error Responses:**

- **400 Bad Request** - Unsupported file type:
```json
{
  "detail": "Unsupported file type. Please upload a PDF or DOCX file."
}
```

- **500 Internal Server Error** - Missing API key:
```json
{
  "detail": "GEMINI_API_KEY not found in environment variables. Please set it in your .env file."
}
```

## Usage Examples

### Using cURL

```bash
# Upload a PDF resume
curl -X POST http://localhost:8000/parse \
  -F "file=@resume.pdf"

# Upload a DOCX resume
curl -X POST http://localhost:8000/parse \
  -F "file=@resume.docx"
```

### Using Python Requests

```python
import requests

# Upload a resume
with open('resume.pdf', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/parse', files=files)

print(response.json())
```

### Using FastAPI Interactive Docs

1. Navigate to: `http://localhost:8000/docs`
2. Find the **POST /parse** endpoint
3. Click **Try it out**
4. Choose a file to upload
5. Click **Execute**

## File Structure Details

### main.py
- FastAPI application setup
- Route definitions (`/` and `/parse`)
- Request validation and error handling
- Response model definition

### gemini_utile.py
- Google Gemini API configuration
- `extract_resume_data()` function
- JSON parsing and validation
- Error handling for API calls

### utils.py
- File validation (`validate_file_type()`)
- Text extraction functions:
  - `extract_text_from_file()`
  - `_extract_text_from_pdf()`
  - `_extract_text_from_docx()`
- File cleanup (`delete_file()`)

## Response Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| **name** | string | Candidate's full name extracted from the resume |
| **tech_stack** | array | List of technologies, programming languages, and tools mentioned in the resume |
| **experience** | float | Total years of professional experience |
| **fit_score** | float | Score from 0-10 based on Python and AI/ML skills match: |
| | | 9-10: Extensive Python and AI/ML expertise |
| | | 7-8: Strong Python and AI/ML skills |
| | | 5-6: Moderate Python and some AI/ML experience |
| | | 3-4: Basic Python knowledge, limited AI/ML |
| | | 0-2: Minimal or no Python/AI skills |

## Dependencies

- **fastapi**: Web framework for building APIs
- **uvicorn**: ASGI server for running FastAPI applications
- **pydantic**: Data validation using Python type annotations
- **python-dotenv**: Load environment variables from .env files
- **pdfplumber**: Extract text from PDF files
- **python-docx**: Read and extract text from DOCX files
- **google-generativeai**: Official Google Gemini API client library

## Error Handling

The API includes comprehensive error handling:

1. **Missing API Key**: Returns 500 error if `GEMINI_API_KEY` is not configured
2. **Unsupported File Type**: Returns 400 error if file is not PDF or DOCX
3. **Empty File**: Returns 400 error if no text can be extracted
4. **API Failures**: Returns 500 error with descriptive message if Gemini API call fails
5. **Invalid JSON Response**: Returns 500 error if API response cannot be parsed

## Troubleshooting

### Issue: "GEMINI_API_KEY not found"
**Solution**: Ensure `.env` file exists in the project root and contains a valid API key.

### Issue: "Unsupported file type"
**Solution**: Only PDF and DOCX files are supported. Ensure your file has the correct extension.

### Issue: "Failed to extract text"
**Solution**: The file may be corrupted or encrypted. Try opening it manually to verify it's readable.

### Issue: "Connection timeout"
**Solution**: Check your internet connection. The Gemini API requires an active internet connection.

### Issue: Port 8000 Already in Use
**Solution**: Use a different port:
```bash
uvicorn main:app --reload --port 8001
```

## Security Considerations

- API keys are loaded from environment variables, not hardcoded
- Temporary files are deleted after processing
- Input validation is performed on all uploaded files
- Error messages are descriptive but don't expose sensitive information

## Performance Notes

- PDF text extraction time depends on file size and complexity
- Gemini API response time typically 2-5 seconds
- Typical request processing time: 3-10 seconds

## Future Enhancements

- Support for additional file formats (TXT, RTF)
- Batch processing for multiple resumes
- Caching of API responses
- Custom skill matching rules
- Resume formatting validation
- Duplicate resume detection

## License

This project is open source and available for educational and commercial use.

## Support

For issues or questions, please refer to:
- FastAPI Documentation: https://fastapi.tiangolo.com
- Google Gemini API: https://ai.google.dev
- pdfplumber: https://github.com/jsvine/pdfplumber
- python-docx: https://python-docx.readthedocs.io
