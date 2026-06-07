"""cursor paginationを小さいlistで理解する練習。"""

from typing import TypedDict


class Item(TypedDict):
    id: str
    created_at: int


class Page(TypedDict):
    items: list[Item]
    next_cursor: str | None


def paginate(items: list[Item], limit: int, after_id: str | None = None) -> Page:
    """created_at昇順のitemsから1ページを返す。limitの最大は100。"""
    # TODO
    raise NotImplementedError
