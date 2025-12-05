"""
FastAPI application for resume parsing and structured data extraction.
Uploads a resume file (PDF/DOCX), extracts text, and uses Google Gemini API
to extract structured resume information.
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from utils import extract_text_from_file, validate_file_type, delete_file
from gemini_utile import extract_resume_data

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI application
app = FastAPI(
    title="Resume Parser API",
    description="Parses resume files and extracts structured data using Google Gemini API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (React, Vite, Postman)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Define the response model for structured resume data
class ResumeResponse(BaseModel):
    """
    Structured response model for resume parsing results.
    """
    name: str
    tech_stack: list[str]
    experience: float
    fit_score: float


@app.get("/")
async def root():
    """
    Root endpoint - returns API information.
    """
    return {
        "message": "Resume Parser API is running",
        "endpoints": {
            "parse": "POST /parse - Upload and parse a resume file"
        }
    }


@app.post("/parse", response_model=ResumeResponse)
async def parse_resume(file: UploadFile = File(...)):
    """
    Main endpoint to parse resume files.
    
    Steps:
    1. Validate the uploaded file type (PDF or DOCX)
    2. Save the file temporarily
    3. Extract text from the file
    4. Delete the temporary file
    5. Send extracted text to Google Gemini API
    6. Return structured resume data
    
    Args:
        file: The uploaded resume file (PDF or DOCX)
    
    Returns:
        ResumeResponse: Structured resume data including name, tech_stack, 
                       experience, and fit_score
    
    Raises:
        HTTPException: If API key is missing, file type is unsupported,
                      or processing fails
    """
    
    # Check if Google Gemini API key is configured
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY not found in environment variables. "
                   "Please set it in your .env file."
        )
    
    # Validate file type
    file_type = validate_file_type(file.filename)
    if not file_type:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type. Please upload a PDF or DOCX file."
        )
    
    # Create temporary file path
    temp_file_path = f"temp_{file.filename}"
    
    try:
        # Save the uploaded file temporarily
        with open(temp_file_path, "wb") as temp_file:
            content = await file.read()
            temp_file.write(content)
        
        # Extract text from the temporary file
        extracted_text = extract_text_from_file(temp_file_path, file_type)
        
        if not extracted_text or extracted_text.strip() == "":
            raise HTTPException(
                status_code=400,
                detail="Failed to extract text from the uploaded file. "
                       "Please ensure the file is valid."
            )
        
        # Send extracted text to Google Gemini API and get structured data
        resume_data = extract_resume_data(extracted_text, api_key)
        
        # Return the structured response
        return ResumeResponse(
            name=resume_data["name"],
            tech_stack=resume_data["tech_stack"],
            experience=resume_data["experience"],
            fit_score=resume_data["fit_score"]
        )
    
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the file: {str(e)}"
        )
    
    finally:
        # Always delete the temporary file, even if an error occurred
        delete_file(temp_file_path)


if __name__ == "__main__":
    # Run the FastAPI application with uvicorn
    # Use: uvicorn main:app --reload
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
