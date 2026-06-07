"""業務ロジックを書く層。"""

from __future__ import annotations

from .model import CreateStudyLogRequest, StudyLog


def validate_request(request: CreateStudyLogRequest) -> list[str]:
    """不正な入力のエラーメッセージを返す。"""
    # TODO
    raise NotImplementedError


def create_study_log(request: CreateStudyLogRequest, next_id: str) -> StudyLog:
    """入力を検証し、StudyLog を作る。不正なら ValueError。"""
    # TODO
    raise NotImplementedError


def total_minutes(logs: list[StudyLog], topic: str | None = None) -> int:
    """topic 指定があればその topic だけ合計する。"""
    # TODO
    raise NotImplementedError


def suggest_next_action(logs: list[StudyLog]) -> str:
    """合計時間に応じて次の行動を返す。"""
    # TODO
    raise NotImplementedError

