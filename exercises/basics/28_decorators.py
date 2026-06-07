"""decorator の基礎練習。"""

from collections.abc import Callable


def add_prefix(prefix: str) -> Callable[[Callable[[], str]], Callable[[], str]]:
    # TODO
    raise NotImplementedError


def call_twice(func: Callable[[], str]) -> Callable[[], list[str]]:
    # TODO
    raise NotImplementedError


def safe_return(default: str) -> Callable[[Callable[[], str]], Callable[[], str]]:
    # TODO
    raise NotImplementedError
