"""FastAPI の request / response schema。"""

from __future__ import annotations

from pydantic import BaseModel, Field


class CreateTaskRequest(BaseModel):
    title: str = Field(min_length=1)
    minutes: int = Field(gt=0)


class TaskResponse(BaseModel):
    id: str
    title: str
    minutes: int
    done: bool
