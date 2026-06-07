from datetime import datetime
from uuid import uuid4

from .ai_client import AIClient
from .model import Review
from .repository import ReviewRepository
from .schema import CreateReviewRequest


def parse_ai_review(text: str) -> tuple[str, list[str]]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return "No review", []
    return lines[0], lines


def create_review(
    request: CreateReviewRequest,
    ai_client: AIClient,
    repository: ReviewRepository,
) -> Review:
    text = ai_client.review(request.code, request.focus)
    summary, suggestions = parse_ai_review(text)
    review = Review(
        id=str(uuid4()),
        code=request.code,
        focus=request.focus,
        summary=summary,
        suggestions=suggestions,
        created_at=datetime.now(),
    )
    repository.save(review)
    return review

