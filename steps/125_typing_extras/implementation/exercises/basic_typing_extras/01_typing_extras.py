"""typing追加要素の基礎練習。"""

from typing import Final, Literal, NewType, cast

UserId = NewType("UserId", str)
type Role = Literal["admin", "member", "viewer"]
DEFAULT_ROLE: Final[Role] = "viewer"


def parse_role(value: str | None) -> Role:
    """文字列をRoleに変換する。不明ならDEFAULT_ROLE。"""
    # TODO
    raise NotImplementedError


def normalize_user_id(value: str) -> UserId:
    """空白を取り除いてUserIdにする。空ならValueError。"""
    # TODO
    raise NotImplementedError


def as_string_list(value: object) -> list[str]:
    """objectを検証してlist[str]として返す。"""
    # TODO
    raise NotImplementedError


def unsafe_cast_example(value: object) -> list[str]:
    """castは検証ではないことを確認するための例。"""
    return cast(list[str], value)
