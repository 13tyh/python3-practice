"""collectionsの基礎練習。"""

from collections import Counter
from collections.abc import Iterable


def count_tags(tags: Iterable[str]) -> Counter[str]:
    """tagごとの件数をCounterで返す。"""
    # TODO
    raise NotImplementedError


def group_names_by_role(users: list[dict[str, str]]) -> dict[str, list[str]]:
    """roleごとにnameをまとめる。"""
    # TODO
    raise NotImplementedError


def recent_items(items: list[str], limit: int) -> list[str]:
    """最後に追加された順に最大limit件を返す。"""
    # TODO
    raise NotImplementedError
