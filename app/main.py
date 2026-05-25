from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.chat import (
    router as chat_router
)

from app.routes.health import (
    router as health_router
)

from app.services.rag_service import (
    load_documents
)

app = FastAPI()

load_documents()

app.include_router(chat_router)
app.include_router(health_router)

app.mount(
    "/",
    StaticFiles(
        directory="frontend",
        html=True
    ),
    name="frontend"
)