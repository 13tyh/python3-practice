"""型ヒントの基礎を厚めに練習。"""

from __future__ import annotations

from typing import Literal, TypedDict


class UserDict(TypedDict):
    id: str
    name: str
    age: int


Status = Literal["active", "inactive", "deleted"]


def get_display_name(name: str | None) -> str:
    # TODO
    raise NotImplementedError


def filter_names(names: list[str | None]) -> list[str]:
    # TODO
    raise NotImplementedError


def count_statuses(statuses: list[Status]) -> dict[Status, int]:
    # TODO
    raise NotImplementedError


def user_label(user: UserDict) -> str:
    # TODO
    raise NotImplementedError

