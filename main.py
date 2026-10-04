import config

from openai import OpenAIError
from fastapi import FastAPI, HTTPException
from orchestrator import run_workflow
from models.request import CodeRequest



app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(data: CodeRequest):
    
    try:
        
        return run_workflow(data.language, data.code)
    
    except OpenAIError:
        
        raise HTTPException(status_code=503, detail="AI service temporarily unavailable.")