# ADVANCED CONFIGURATION GUIDE

This file shows how to customize and extend the Resume Parser API.

## Customizing the Gemini Prompt

Edit the `prompt` variable in `gemini_utile.py` to change what data is extracted.

### Example 1: Extract Salary Requirements

```python
prompt = f"""
    Extract structured information from the following resume text in JSON format.
    
    IMPORTANT: Return ONLY valid JSON, nothing else.
    
    Extract exactly these fields:
    - "name": The candidate's full name (string)
    - "tech_stack": A list of technologies and tools mentioned (list)
    - "experience": Total years of professional experience (float)
    - "fit_score": Score 0-10 based on Python and AI/ML skills (float)
    - "salary_expectation": Estimated salary expectation if mentioned (string or null)
    
    Resume text:
    {resume_text}
    
    Return ONLY the JSON object, no additional text.
    """
```

### Example 2: Extract Certifications and Education

```python
prompt = f"""
    Extract structured information from the following resume text in JSON format.
    
    IMPORTANT: Return ONLY valid JSON, nothing else.
    
    Extract exactly these fields:
    - "name": The candidate's full name (string)
    - "tech_stack": Technologies and tools (list)
    - "experience": Years of professional experience (float)
    - "fit_score": Score 0-10 based on Python and AI/ML (float)
    - "education": List of degrees and universities (list)
    - "certifications": Professional certifications (list)
    
    Resume text:
    {resume_text}
    
    Return ONLY the JSON object, no additional text.
    """
```

### Example 3: Industry-Specific Scoring

For finance professionals:

```python
prompt = f"""
    Extract structured information from the following resume text in JSON format.
    
    IMPORTANT: Return ONLY valid JSON, nothing else.
    
    Extract exactly these fields:
    - "name": The candidate's full name (string)
    - "tech_stack": Technologies and tools (list)
    - "experience": Years of professional experience (float)
    - "fit_score": Score 0-10 based on:
      * Knowledge of financial systems (Bloomberg, Reuters, etc.)
      * Python/C++ for quantitative analysis
      * Machine Learning for algorithmic trading
      * Risk management expertise
      * 9-10: Expert in multiple financial technologies
      * 7-8: Strong financial domain knowledge
      * 5-6: Moderate financial experience
      * 3-4: Basic understanding
      * 0-2: No relevant experience
    
    Resume text:
    {resume_text}
    
    Return ONLY the JSON object, no additional text.
    """
```

## Modifying the Response Model

Edit the `ResumeResponse` class in `main.py` to add new fields:

```python
class ResumeResponse(BaseModel):
    """Extended resume response model."""
    name: str
    tech_stack: list[str]
    experience: float
    fit_score: float
    salary_expectation: str | None = None  # NEW
    education: list[str] | None = None     # NEW
    certifications: list[str] | None = None # NEW
```

Then update the return statement in the `/parse` endpoint:

```python
return ResumeResponse(
    name=resume_data["name"],
    tech_stack=resume_data["tech_stack"],
    experience=resume_data["experience"],
    fit_score=resume_data["fit_score"],
    salary_expectation=resume_data.get("salary_expectation"),  # NEW
    education=resume_data.get("education"),                      # NEW
    certifications=resume_data.get("certifications")             # NEW
)
```

## Environment-Specific Configurations

Create different `.env` files for different environments:

### `.env.development`
```
GEMINI_API_KEY=your_dev_key_here
DEBUG=True
```

### `.env.production`
```
GEMINI_API_KEY=your_prod_key_here
DEBUG=False
```

Load the appropriate file:

```python
from dotenv import load_dotenv
import os

env = os.getenv("ENVIRONMENT", "development")
load_dotenv(f".env.{env}")
```

## Extending with Additional Endpoints

### Example: Batch Processing Multiple Resumes

```python
@app.post("/batch-parse")
async def batch_parse_resumes(files: list[UploadFile] = File(...)):
    """Parse multiple resume files at once."""
    results = []
    
    for file in files:
        try:
            # Reuse existing parse logic
            file_type = validate_file_type(file.filename)
            if not file_type:
                continue
            
            temp_path = f"temp_{file.filename}"
            with open(temp_path, "wb") as f:
                f.write(await file.read())
            
            text = extract_text_from_file(temp_path, file_type)
            api_key = os.getenv("GEMINI_API_KEY")
            data = extract_resume_data(text, api_key)
            
            results.append({
                "filename": file.filename,
                "data": data
            })
            
            delete_file(temp_path)
        
        except Exception as e:
            results.append({
                "filename": file.filename,
                "error": str(e)
            })
    
    return results
```

### Example: Scoring Endpoint

```python
@app.post("/score")
async def score_resume(resume_data: ResumeResponse):
    """Custom scoring logic based on job requirements."""
    
    # Define required skills
    required_skills = {
        "Python": 10,
        "FastAPI": 5,
        "Machine Learning": 8,
        "Docker": 3
    }
    
    score = 0
    matched_skills = []
    
    for skill, weight in required_skills.items():
        if skill in resume_data.tech_stack:
            score += weight
            matched_skills.append(skill)
    
    max_score = sum(required_skills.values())
    percentage = (score / max_score) * 100
    
    return {
        "match_score": percentage,
        "matched_skills": matched_skills,
        "missing_skills": [s for s in required_skills if s not in matched_skills]
    }
```

## Performance Optimization

### Caching Results

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_gemini_response(resume_hash: str):
    """Cache Gemini API responses to reduce API calls."""
    pass
```

### Async Text Extraction

```python
import asyncio

async def extract_text_async(file_path: str, file_type: str):
    """Non-blocking text extraction."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, extract_text_from_file, file_path, file_type)
```

## Database Integration

Store parsed resumes in a database:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./resumes.db"
engine = create_engine(DATABASE_URL)

# Create tables and models as needed
```

## Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t resume-parser .
docker run -p 8000:8000 --env-file .env resume-parser
```

## Monitoring and Logging

Add logging to track API usage:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/parse")
async def parse_resume(file: UploadFile = File(...)):
    logger.info(f"Processing resume: {file.filename}")
    # ... rest of the code
    logger.info(f"Successfully parsed: {file.filename}")
```

## Rate Limiting

Prevent API abuse:

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.post("/parse")
@limiter.limit("5/minute")
async def parse_resume(request: Request, file: UploadFile = File(...)):
    # ... rest of the code
```

## Error Tracking

Integrate with error tracking services:

```python
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

sentry_sdk.init(
    dsn="your_sentry_dsn_here",
    integrations=[FastApiIntegration()],
)
```

## Next Steps

1. **Choose customizations** that fit your use case
2. **Test thoroughly** before deploying to production
3. **Monitor performance** and adjust as needed
4. **Document changes** for your team

For more information:
- FastAPI: https://fastapi.tiangolo.com
- Google Gemini: https://ai.google.dev
- SQLAlchemy: https://www.sqlalchemy.org
- Docker: https://www.docker.com
