"""FastAPI の router。"""

from __future__ import annotations

from fastapi import APIRouter, status

from .schema import CreateTaskRequest, TaskResponse
from .service import TaskStore


def create_router(store: TaskStore) -> APIRouter:
    router = APIRouter(prefix="/tasks", tags=["tasks"])

    @router.get("", response_model=list[TaskResponse])
    def get_tasks() -> list[TaskResponse]:
        # TODO
        raise NotImplementedError

    @router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
    def post_task(request: CreateTaskRequest) -> TaskResponse:
        # TODO
        raise NotImplementedError

    @router.patch("/{task_id}/done", response_model=TaskResponse)
    def patch_done(task_id: str) -> TaskResponse:
        # TODO
        raise NotImplementedError

    return router
