"""解答例: exercises/fastapi_ai_app/service.py."""

from exercises.fastapi_ai_app.schema import ChatRequest, ChatResponse, CodeReviewRequest, CodeReviewResponse
from exercises.fastapi_ai_app.service import TextGenerator


def build_review_prompt(request: CodeReviewRequest) -> str:
    return f"Focus: {request.focus}\nReview this Python code:\n{request.code}"


def parse_suggestions(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def review_code(generator: TextGenerator, request: CodeReviewRequest) -> CodeReviewResponse:
    text = generator.invoke(build_review_prompt(request))
    suggestions = parse_suggestions(text)
    summary = suggestions[0] if suggestions else "No suggestions"
    return CodeReviewResponse(summary=summary, suggestions=suggestions)


def chat(generator: TextGenerator, request: ChatRequest) -> ChatResponse:
    return ChatResponse(reply=generator.invoke(request.message))

