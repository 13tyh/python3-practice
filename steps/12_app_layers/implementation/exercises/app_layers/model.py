"""データの形を定義する層。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StudyLog:
    id: str
    topic: str
    minutes: int
    memo: str


@dataclass(frozen=True)
class CreateStudyLogRequest:
    topic: str
    minutes: int
    memo: str


@dataclass(frozen=True)
class StudyLogResponse:
    id: str
    title: str
    minutes: int
