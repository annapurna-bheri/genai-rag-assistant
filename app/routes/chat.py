from fastapi import APIRouter
from pydantic import BaseModel

from app.services.rag_service import chat

router = APIRouter()

class ChatRequest(BaseModel):
    sessionId: str
    message: str

@router.post("/api/chat")
def chat_api(request: ChatRequest):

    if not request.message:

        return {
            "error":
            "Message field is required"
        }

    response = chat(
        request.sessionId,
        request.message
    )

    return response