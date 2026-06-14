"""itertools / functoolsの基礎練習。"""

from collections.abc import Callable, Iterable
from functools import lru_cache


def group_sorted_pairs(pairs: list[tuple[str, int]]) -> dict[str, list[int]]:
    """keyでsort済みのpairをgroupbyでまとめる。"""
    # TODO
    raise NotImplementedError


def make_multiplier(n: int) -> Callable[[int], int]:
    """partialでn倍する関数を返す。"""
    # TODO
    raise NotImplementedError


@lru_cache(maxsize=32)
def fibonacci(n: int) -> int:
    """再帰とcacheでfibonacciを返す。"""
    # TODO
    raise NotImplementedError


def flatten(nested: Iterable[Iterable[str]]) -> list[str]:
    """二重iterableを平らなlistにする。"""
    # TODO
    raise NotImplementedError
