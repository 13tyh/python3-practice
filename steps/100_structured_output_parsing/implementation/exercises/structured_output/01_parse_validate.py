"""AI structured outputを検証する練習。"""

from typing import Any


def parse_json_object(text: str) -> dict[str, Any] | None:
    """JSON objectならdict、失敗ならNoneを返す。"""
    # TODO
    raise NotImplementedError


def missing_required_keys(data: dict[str, Any], required: set[str]) -> list[str]:
    """不足しているrequired keyを返す。"""
    # TODO
    raise NotImplementedError


def is_valid_output(text: str, required: set[str]) -> bool:
    """JSON objectかつrequiredを満たすならTrue。"""
    # TODO
    raise NotImplementedError
