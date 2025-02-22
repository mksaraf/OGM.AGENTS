from fastapi import FastAPI
from crew import ContentCrew

fast_app = FastAPI()

@app.post("/generate_content")
def generate_content(topic: str):
    crew = ContentCrew()
    result = crew.kickoff(inputs={"topic": topic})
    return {"result": result}