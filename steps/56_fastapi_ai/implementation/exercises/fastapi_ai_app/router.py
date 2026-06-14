"""FastAPI router for AI endpoints."""

from __future__ import annotations

from fastapi import APIRouter

from .schema import ChatRequest, ChatResponse, CodeReviewRequest, CodeReviewResponse
from .service import TextGenerator


def create_router(generator: TextGenerator) -> APIRouter:
    router = APIRouter(prefix="/ai", tags=["ai"])

    @router.post("/review", response_model=CodeReviewResponse)
    def post_review(request: CodeReviewRequest) -> CodeReviewResponse:
        # TODO
        raise NotImplementedError

    @router.post("/chat", response_model=ChatResponse)
    def post_chat(request: ChatRequest) -> ChatResponse:
        # TODO
        raise NotImplementedError

    return router
