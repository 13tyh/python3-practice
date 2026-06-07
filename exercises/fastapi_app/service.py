"""FastAPI app の業務ロジック。"""

from __future__ import annotations

from dataclasses import dataclass

from .schema import CreateTaskRequest, TaskResponse


@dataclass
class TaskStore:
    tasks: dict[str, TaskResponse]


def create_store() -> TaskStore:
    # TODO
    raise NotImplementedError


def create_task(store: TaskStore, request: CreateTaskRequest) -> TaskResponse:
    # TODO
    raise NotImplementedError


def list_tasks(store: TaskStore) -> list[TaskResponse]:
    # TODO
    raise NotImplementedError


def mark_done(store: TaskStore, task_id: str) -> TaskResponse | None:
    # TODO
    raise NotImplementedError

