"""
Google Gemini API utility for extracting structured resume data.
Sends extracted resume text to Google Gemini API and parses the response
into structured JSON format.
"""

import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def extract_resume_data(resume_text: str, api_key: str) -> dict:
    """
    Sends resume text to Google Gemini API and extracts structured data.
    
    Args:
        resume_text: Raw text extracted from the resume file
        api_key: Google Gemini API key from environment variables
    
    Returns:
        dict: Structured resume data containing:
            - name: str (candidate's full name)
            - tech_stack: list[str] (technologies and skills)
            - experience: float (total years of experience)
            - fit_score: float (0-10 score based on Python + AI skills)
    
    Raises:
        ValueError: If the API response is invalid or cannot be parsed
        Exception: If the API call fails
    """
    
    # Configure the Gemini API with the provided API key
    genai.configure(api_key=api_key)
    
    # Create the prompt for Gemini to extract resume data
    prompt = f"""
    Extract structured information from the following resume text in JSON format.
    
    IMPORTANT: Return ONLY valid JSON, nothing else. No markdown, no code blocks.
    
    Extract exactly these fields:
    - "name": The candidate's full name (string)
    - "tech_stack": A list of technologies, programming languages, and tools mentioned (list of strings)
    - "experience": Total years of professional experience as a number (float)
    - "fit_score": A score from 0-10 based on how well the candidate matches Python and AI skills:
      * 9-10: Extensive Python and AI/ML expertise
      * 7-8: Strong Python and AI/ML skills
      * 5-6: Moderate Python and some AI/ML experience
      * 3-4: Basic Python knowledge, limited AI/ML
      * 0-2: Minimal or no Python/AI skills
    
    Resume text:
    {resume_text}
    
    Return ONLY the JSON object, no additional text.
    """
    
    # Call the Gemini API
    try:
        # Use the correct model name with v1 API
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)
        
        # Extract the text response from Gemini
        response_text = response.text.strip()
        
        # Remove markdown code blocks if present
        if response_text.startswith("```"):
            # Find the end of the code block
            end_marker = response_text.find("```", 3)
            if end_marker != -1:
                response_text = response_text[3:end_marker]
            # Remove json language specifier if present
            if response_text.startswith("json"):
                response_text = response_text[4:]
        
        response_text = response_text.strip()
        
        # Parse the JSON response
        resume_data = json.loads(response_text)
        
        # Validate and normalize the response data
        resume_data = {
            "name": resume_data.get("name", "Unknown"),
            "tech_stack": resume_data.get("tech_stack", []),
            "experience": float(resume_data.get("experience", 0)),
            "fit_score": float(resume_data.get("fit_score", 0))
        }
        
        # Ensure fit_score is within valid range (0-10)
        resume_data["fit_score"] = max(0, min(10, resume_data["fit_score"]))
        
        return resume_data
    
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Failed to parse Gemini API response as JSON: {e}. "
            f"Response text: {response_text}"
        )
    except Exception as e:
        raise Exception(
            f"Error calling Google Gemini API: {str(e)}"
        )
