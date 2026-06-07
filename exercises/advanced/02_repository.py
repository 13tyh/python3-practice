"""Repository パターンの応用。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    id: str
    title: str
    done: bool = False


class InMemoryTaskRepository:
    def __init__(self) -> None:
        # TODO
        raise NotImplementedError

    def add(self, task: Task) -> None:
        # TODO
        raise NotImplementedError

    def find_by_id(self, task_id: str) -> Task | None:
        # TODO
        raise NotImplementedError

    def list_all(self) -> list[Task]:
        # TODO
        raise NotImplementedError

    def mark_done(self, task_id: str) -> Task:
        # TODO
        raise NotImplementedError
