import json
from pathlib import Path

from .schema import CreateReviewRequest


def build_jsonl(items: list[CreateReviewRequest]) -> str:
    lines = []
    for index, item in enumerate(items, start=1):
        lines.append(json.dumps({"id": str(index), "code": item.code, "focus": item.focus}))
    return "\n".join(lines) + "\n"


def write_jsonl(path: Path, items: list[CreateReviewRequest]) -> None:
    path.write_text(build_jsonl(items), encoding="utf-8")
