"""Request / response schema for FastAPI AI app."""

from __future__ import annotations

from pydantic import BaseModel, Field


class CodeReviewRequest(BaseModel):
    code: str = Field(min_length=1)
    focus: str = "bug"


class CodeReviewResponse(BaseModel):
    summary: str
    suggestions: list[str]


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)


class ChatResponse(BaseModel):
    reply: str

