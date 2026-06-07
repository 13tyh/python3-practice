"""AI service layer.

LangChain の chain や Runnable を直接 router に置かず、この層に閉じ込める練習。
"""

from __future__ import annotations

from typing import Protocol

from .schema import ChatRequest, ChatResponse, CodeReviewRequest, CodeReviewResponse


class TextGenerator(Protocol):
    def invoke(self, prompt: str) -> str:
        """Return generated text for prompt."""


class FakeTextGenerator:
    def invoke(self, prompt: str) -> str:
        return f"fake response: {prompt[:30]}"


def build_review_prompt(request: CodeReviewRequest) -> str:
    # TODO
    raise NotImplementedError


def parse_suggestions(text: str) -> list[str]:
    # TODO
    raise NotImplementedError


def review_code(generator: TextGenerator, request: CodeReviewRequest) -> CodeReviewResponse:
    # TODO
    raise NotImplementedError


def chat(generator: TextGenerator, request: ChatRequest) -> ChatResponse:
    # TODO
    raise NotImplementedError
