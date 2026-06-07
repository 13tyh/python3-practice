"""background jobの状態管理練習。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Job:
    id: str
    status: str
    idempotency_key: str


def create_job(existing: list[Job], job_id: str, idempotency_key: str) -> Job | None:
    """同じidempotency_keyがある場合はNoneを返す。"""
    # TODO
    raise NotImplementedError


def next_pending_job(jobs: list[Job]) -> Job | None:
    """最初のpending jobを返す。"""
    # TODO
    raise NotImplementedError


def complete_job(job: Job, succeeded: bool) -> Job:
    """jobをsucceeded/failedへ更新した新しいJobを返す。"""
    # TODO
    raise NotImplementedError
