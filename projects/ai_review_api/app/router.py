from fastapi import APIRouter

from .ai_client import AIClient
from .batch import build_jsonl
from .repository import ReviewRepository
from .schema import BatchReviewRequest, CreateReviewRequest, ReviewResponse
from .service import create_review


def create_router(ai_client: AIClient, repository: ReviewRepository) -> APIRouter:
    router = APIRouter()

    @router.post("/reviews", response_model=ReviewResponse)
    def post_review(request: CreateReviewRequest) -> ReviewResponse:
        review = create_review(request, ai_client, repository)
        return ReviewResponse(id=review.id, summary=review.summary, suggestions=review.suggestions)

    @router.get("/reviews", response_model=list[ReviewResponse])
    def get_reviews() -> list[ReviewResponse]:
        return [
            ReviewResponse(id=item.id, summary=item.summary, suggestions=item.suggestions)
            for item in repository.list_reviews()
        ]

    @router.post("/batch/reviews")
    def post_batch(request: BatchReviewRequest) -> dict[str, str]:
        return {"jsonl": build_jsonl(request.items)}

    return router
