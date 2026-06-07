"""DB query 作成の練習。"""

from __future__ import annotations


def build_date_range_query(start: str | None, end: str | None) -> dict[str, object]:
    """created_at の範囲 query を作る。"""
    # TODO
    raise NotImplementedError


def build_projection(fields: list[str]) -> dict[str, int]:
    """MongoDB projection を作る。_id は除外する。"""
    # TODO
    raise NotImplementedError


def build_sort(field: str, descending: bool = False) -> list[tuple[str, int]]:
    # TODO
    raise NotImplementedError
