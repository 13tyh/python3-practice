from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Review:
    id: str
    code: str
    focus: str
    summary: str
    suggestions: list[str]
    created_at: datetime
