"""union型を安全に絞り込む練習。"""

from typing import TypedDict


class RawUser(TypedDict, total=False):
    name: str
    age: int | str | None
    active: bool


class NormalizedUser(TypedDict):
    name: str
    age: int
    active: bool


def parse_age(value: int | str | None) -> int | None:
    """年齢として扱える値だけintで返す。"""
    # TODO
    raise NotImplementedError


def normalize_user(user: RawUser) -> NormalizedUser | None:
    """nameとageが有効なuserだけ正規化して返す。"""
    # TODO
    raise NotImplementedError
