"""API 設計の練習。"""


def build_pagination(page: int, per_page: int, total: int) -> dict[str, int | bool]:
    # TODO
    raise NotImplementedError


def parse_sort(sort: str | None, allowed_fields: set[str]) -> tuple[str, str]:
    """例: -created_at -> (created_at, desc)。"""
    # TODO
    raise NotImplementedError


def error_response(code: str, message: str, status_code: int) -> dict[str, object]:
    # TODO
    raise NotImplementedError


def idempotency_cache_key(method: str, path: str, key: str) -> str:
    # TODO
    raise NotImplementedError

