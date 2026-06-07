"""外部 API client 設計。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ApiClientConfig:
    base_url: str
    timeout_seconds: int
    max_retries: int


def build_url(config: ApiClientConfig, path: str) -> str:
    # TODO
    raise NotImplementedError


def should_retry_status(status_code: int) -> bool:
    # TODO
    raise NotImplementedError


def backoff_seconds(attempt: int) -> int:
    # TODO
    raise NotImplementedError
