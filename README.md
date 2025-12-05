# Resume Screening Application

A full-stack application for parsing and screening resumes with AI-powered analysis. This project combines a **FastAPI backend** for resume parsing with a **React + Vite frontend** for an intuitive user interface.

---

## 🎯 Project Overview

This application automates the resume screening process by:
- Uploading and parsing resume files (PDF/DOCX)
- Extracting structured candidate information using Google Gemini AI
- Displaying parsed data with skill-based fit scores
- Providing a modern, responsive web interface

**Technology Stack:**
- **Backend:** FastAPI, Python, Google Gemini API
- **Frontend:** React 19, Vite, Tailwind CSS, Axios
- **File Processing:** pdfplumber, python-docx

---

## 📁 Project Structure

```
resume-screening/
├── backend/                    # FastAPI application
│   ├── main.py                # FastAPI app & endpoints
│   ├── gemini_utile.py        # Google Gemini API integration
│   ├── model.py               # Data models
│   ├── utils.py               # File handling utilities
│   ├── utils/                 # Additional utilities
│   │   ├── extract_ai.py      # AI extraction logic
│   │   ├── experience.py      # Experience parsing
│   │   └── score.py           # Scoring calculations
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example           # Environment variables template
│   └── README.md              # Backend documentation
│
├── resume-frontend/           # React + Vite application
│   ├── src/
│   │   ├── main.jsx           # Entry point
│   │   ├── App.jsx            # Main component
│   │   ├── components/        # React components
│   │   │   ├── ResumeUploader.jsx
│   │   │   └── ParsedResumeResult.jsx
│   │   ├── index.css          # Styles
│   │   └── assets/
│   ├── package.json           # NPM dependencies
│   ├── vite.config.js         # Vite configuration
│   ├── tailwind.config.js     # Tailwind CSS config
│   └── README.md              # Frontend documentation
│
└── README.md                  # This file (main project guide)
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** (for backend)
- **Node.js 16+** (for frontend)
- **Google Gemini API Key** (get it from [aistudio.google.com](https://aistudio.google.com/app/apikey))

### Backend Setup

```bash
# 1. Navigate to backend folder
cd backend

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create .env file
cp .env.example .env
# Edit .env and add: GEMINI_API_KEY=your_api_key_here

# 6. Run the application
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Backend URL:** `http://localhost:8000`

### Frontend Setup

```bash
# 1. Navigate to frontend folder (from project root)
cd resume-frontend

# 2. Install dependencies
npm install

# 3. Run development server
npm run dev
```

**Frontend URL:** `http://localhost:5173` (or as shown in terminal)

---

## 📡 API Documentation

### Swagger UI (Interactive API Documentation)

Once the backend is running, access the interactive Swagger documentation at:

```
http://localhost:8000/docs
```

This provides:
- ✅ All available endpoints
- ✅ Request/response schemas
- ✅ Live API testing interface
- ✅ Detailed parameter descriptions

### Alternative: ReDoc Documentation

```
http://localhost:8000/redoc
```

---

## 🔌 API Endpoints

### 1. **Root Endpoint**

```http
GET /
```

**Response:**
```json
{
  "message": "Resume Parser API is running",
  "endpoints": {
    "parse": "POST /parse - Upload and parse a resume file"
  }
}
```

---

### 2. **Parse Resume Endpoint** ⭐

```http
POST /parse
```

**Request:** Multipart form data with file upload

**Parameters:**
- `file` (required): Resume file in PDF or DOCX format

**Response Model:**
```json
{
  "name": "John Doe",
  "tech_stack": ["Python", "FastAPI", "React", "JavaScript"],
  "experience": 5.5,
  "fit_score": 0.87
}
```

**Response Fields:**
- `name`: Extracted candidate name
- `tech_stack`: List of identified technologies and skills
- `experience`: Years of professional experience
- `fit_score`: AI-calculated skill match score (0-1)

**Status Codes:**
- `200`: Success - Resume parsed successfully
- `400`: Bad Request - Invalid file type or missing file
- `500`: Server Error - API key missing or processing error

**Example Using cURL:**
```bash
curl -X POST "http://localhost:8000/parse" \
  -H "accept: application/json" \
  -F "file=@resume.pdf"
```

**Example Using Python:**
```python
import requests

with open("resume.pdf", "rb") as f:
    files = {"file": f}
    response = requests.post("http://localhost:8000/parse", files=files)
    print(response.json())
```

**Example Using JavaScript (Axios):**
```javascript
const formData = new FormData();
formData.append("file", fileInput.files[0]);

const response = await axios.post("http://localhost:8000/parse", formData, {
  headers: { "Content-Type": "multipart/form-data" }
});

console.log(response.data);
```

---

## 🛠️ Backend Technologies

| Technology | Purpose | Version |
|-----------|---------|---------|
| **FastAPI** | Web framework | 0.123.9 |
| **Uvicorn** | ASGI server | 0.38.0 |
| **Pydantic** | Data validation | 2.12.5 |
| **pdfplumber** | PDF text extraction | ≥0.9.0 |
| **python-docx** | DOCX text extraction | ≥0.8.11 |
| **google-generativeai** | Gemini API client | ≥0.8.0 |
| **python-dotenv** | Environment variables | 1.2.1 |

---

## 🎨 Frontend Technologies

| Technology | Purpose | Version |
|-----------|---------|---------|
| **React** | UI framework | 19.2.0 |
| **Vite** | Build tool | 7.2.4 |
| **Tailwind CSS** | Styling | 3.4.18 |
| **Axios** | HTTP client | 1.13.2 |
| **Framer Motion** | Animations | 12.23.25 |
| **Lucide React** | Icons | 0.556.0 |

---

## 🔐 Environment Setup

### Backend Environment Variables

Create a `.env` file in the `backend` folder:

```env
# Google Gemini API Configuration
GEMINI_API_KEY=your_actual_api_key_here

# Optional: API Server Configuration
API_HOST=0.0.0.0
API_PORT=8000
```

**Getting Your Gemini API Key:**
1. Visit https://aistudio.google.com/app/apikey
2. Click "Create API key"
3. Copy the key and paste it in `.env`

---

## 📊 Key Features

### Backend Features
- ✅ **Multi-format Support:** PDF and DOCX resume parsing
- ✅ **AI-Powered Extraction:** Google Gemini API for intelligent data extraction
- ✅ **Structured Output:** JSON response with all resume details
- ✅ **Error Handling:** Comprehensive error messages
- ✅ **CORS Enabled:** Works seamlessly with React frontend
- ✅ **Auto Cleanup:** Temporary files automatically deleted after processing
- ✅ **Interactive Docs:** Swagger UI for API testing

### Frontend Features
- ✅ **Drag & Drop Upload:** Easy file selection
- ✅ **Real-time Preview:** View parsed resume data instantly
- ✅ **Responsive Design:** Works on desktop, tablet, and mobile
- ✅ **Skill Visualization:** Display extracted tech stack
- ✅ **Fit Score Display:** Visual representation of candidate match
- ✅ **Error Handling:** User-friendly error messages
- ✅ **Smooth Animations:** Framer Motion for polished UX

---

## 🧪 Testing

### Backend Testing

**Using Swagger UI:**
1. Navigate to `http://localhost:8000/docs`
2. Click on the `/parse` endpoint
3. Click "Try it out"
4. Upload a resume file
5. Click "Execute"

**Using cURL:**
```bash
curl -X POST "http://localhost:8000/parse" \
  -F "file=@your_resume.pdf"
```

**Using Python:**
```bash
# Run test script
python test_api.py
```

### Frontend Testing

1. Open `http://localhost:5173`
2. Upload a resume file using the drag & drop area
3. View the parsed results in real-time

---

## 🚨 Troubleshooting

### Backend Issues

**Error: "GEMINI_API_KEY not found"**
- ✅ Create `.env` file in the `backend` folder
- ✅ Add your API key: `GEMINI_API_KEY=your_key_here`
- ✅ Restart the server

**Error: "Unsupported file type"**
- ✅ Ensure you're uploading PDF or DOCX files
- ✅ Check file isn't corrupted

**Port Already in Use:**
```bash
# Use a different port
uvicorn main:app --reload --port 8001
```

### Frontend Issues

**Blank Page / No Results**
- ✅ Ensure backend is running on `http://localhost:8000`
- ✅ Check browser console for errors
- ✅ Clear browser cache and reload

**CORS Errors**
- ✅ Backend has CORS enabled for all origins
- ✅ Ensure backend is running before frontend

---

## 📚 Additional Documentation

- **Backend Guide:** See `backend/README.md` for detailed backend documentation
- **Frontend Guide:** See `resume-frontend/README.md` for frontend details
- **API Documentation:** Access `http://localhost:8000/docs` when backend is running

---

## 🔄 Development Workflow

### Running Both Services

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate  # or source venv/bin/activate
uvicorn main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd resume-frontend
npm run dev
```

---

## 📦 Build & Deployment

### Backend Build
```bash
# Production run
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Frontend Build
```bash
cd resume-frontend
npm run build  # Creates optimized build in dist/
npm run preview  # Preview production build
```

---

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit pull request

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🔗 Useful Links

- **Google Gemini API:** https://aistudio.google.com
- **FastAPI Docs:** https://fastapi.tiangolo.com
- **React Docs:** https://react.dev
- **Vite Docs:** https://vitejs.dev
- **Tailwind CSS:** https://tailwindcss.com

---

## 💡 Tips

- **Test API endpoints** using Swagger UI at `http://localhost:8000/docs`
- **Monitor backend logs** to debug issues
- **Use browser DevTools** to debug frontend issues
- **Keep API key secure** - Never commit `.env` file
- **Install dependencies** before running either service

---

**Last Updated:** December 5, 2025

For questions or issues, check the backend and frontend README files for more detailed information.
