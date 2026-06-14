"""Protocol / Generic / TypeGuard の練習。"""

from __future__ import annotations

from typing import Generic, Protocol, TypeGuard, TypeVar


class HasName(Protocol):
    name: str


T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        # TODO
        raise NotImplementedError

    def get(self) -> T:
        # TODO
        raise NotImplementedError


def greet_named(value: HasName) -> str:
    # TODO
    raise NotImplementedError


def is_str_list(value: object) -> TypeGuard[list[str]]:
    # TODO
    raise NotImplementedError
