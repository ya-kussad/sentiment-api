from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests
import os

app = FastAPI()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434/api/generate")

# Serve static files from the "static" directory (containing index.html)
app.mount("/static", StaticFiles(directory="static"), name="static")

class Summary(BaseModel):
    prompt: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.post("/generate")
def analyze_sentiment(request: Summary):
    prompt = f"""Determine the sentiment (Positive, Neutral, or Negative) of the following text:
"{request.prompt}"
Respond with just one word."""

    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_HOST, json=payload)
    response.raise_for_status()

    result = response.json()["response"].strip().lower()
    
    if "positive" in result:
        sentiment = "Positive"
    elif "negative" in result:
        sentiment = "Negative"
    elif "neutral" in result:
        sentiment = "Neutral"
    else:
        sentiment = "Neutral"

    return {"sentiment": sentiment}

