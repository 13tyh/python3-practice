"""外側との接点を担当する層。FastAPI の router を単純化した練習版。"""

from __future__ import annotations

from typing import Any

from .model import CreateStudyLogRequest, StudyLog, StudyLogResponse
from .service import create_study_log, suggest_next_action


def to_response(log: StudyLog) -> StudyLogResponse:
    """内部 model を外向き response に変換する。"""
    # TODO
    raise NotImplementedError


def create_log_endpoint(payload: dict[str, Any], next_id: str) -> dict[str, Any]:
    """dict の入力を受け、service を呼び、dict の response を返す。"""
    # TODO
    raise NotImplementedError


def next_action_endpoint(logs: list[StudyLog]) -> dict[str, str]:
    """次の行動を返す endpoint。"""
    # TODO
    raise NotImplementedError

