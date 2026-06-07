from fastapi import FastAPI

from .ai_client import FakeAIClient
from .repository import InMemoryReviewRepository
from .router import create_router


def create_app() -> FastAPI:
    app = FastAPI(title="AI Review API")
    app.include_router(create_router(FakeAIClient(), InMemoryReviewRepository()))
    return app


app = create_app()

