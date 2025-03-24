from fastapi import FastAPI
from pydantic import BaseModel
from .services import get_legal_advice


app = FastAPI()

class ChatRequest(BaseModel):
    question: str
    session_id: str

class ChatResponse(BaseModel):
    answer: str

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = get_legal_advice(request.question, request.session_id)
    return {"answer": answer}
