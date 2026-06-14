"""ジョブキューの基礎。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

JobStatus = Literal["queued", "running", "succeeded", "failed"]


@dataclass
class Job:
    id: str
    payload: dict[str, str]
    status: JobStatus = "queued"
    attempts: int = 0


def enqueue(queue: list[Job], job: Job) -> None:
    # TODO
    raise NotImplementedError


def mark_running(job: Job) -> None:
    # TODO
    raise NotImplementedError


def should_retry(job: Job, max_attempts: int) -> bool:
    # TODO
    raise NotImplementedError
