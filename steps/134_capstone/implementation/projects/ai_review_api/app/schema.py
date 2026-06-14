from pydantic import BaseModel, Field


class CreateReviewRequest(BaseModel):
    code: str = Field(min_length=1)
    focus: str = "bug"


class ReviewResponse(BaseModel):
    id: str
    summary: str
    suggestions: list[str]


class BatchReviewRequest(BaseModel):
    items: list[CreateReviewRequest]
