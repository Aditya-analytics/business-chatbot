from fastapi import FastAPI
from pydantic import BaseModel
from app.services.llm_service import generate_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    reply = generate_response(request.message)
    return {"response": reply}
