from pydantic import BaseModel


class ResumeInput(BaseModel):
    resume_text:str
    
class ResumeOutput(BaseModel):
    name: str
    tech_stack: list
    years_of_experience: float
    fit_score: float