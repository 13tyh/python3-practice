"""observability の基礎。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class RequestContext:
    request_id: str
    user_id: str | None
    path: str


def build_log_event(context: RequestContext, action: str, status: str) -> dict[str, str]:
    # TODO
    raise NotImplementedError


def metric_name(service: str, action: str, metric: str) -> str:
    # TODO
    raise NotImplementedError


def trace_parent(child_span: str, parent_span: str | None) -> dict[str, str]:
    # TODO
    raise NotImplementedError

