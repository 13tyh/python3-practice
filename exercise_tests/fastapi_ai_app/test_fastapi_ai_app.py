from fastapi.testclient import TestClient

from exercises.fastapi_ai_app.main import create_app
from exercises.fastapi_ai_app.schema import CodeReviewRequest
from exercises.fastapi_ai_app.service import build_review_prompt, parse_suggestions


def test_build_review_prompt() -> None:
    prompt = build_review_prompt(CodeReviewRequest(code="print('x')", focus="security"))
    assert "security" in prompt
    assert "print('x')" in prompt


def test_parse_suggestions() -> None:
    assert parse_suggestions("one\ntwo\n\nthree") == ["one", "two", "three"]


def test_fastapi_ai_flow() -> None:
    client = TestClient(create_app())

    review = client.post("/ai/review", json={"code": "print('x')", "focus": "bug"})
    assert review.status_code == 200
    body = review.json()
    assert body["summary"]
    assert isinstance(body["suggestions"], list)

    chat = client.post("/ai/chat", json={"message": "hello"})
    assert chat.status_code == 200
    assert chat.json()["reply"]

