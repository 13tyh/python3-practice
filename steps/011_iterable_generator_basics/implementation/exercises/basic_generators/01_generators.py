"""generatorの基礎練習。"""

from collections.abc import Iterable, Iterator


def count_up_to(limit: int) -> Iterator[int]:
    """0からlimit未満までyieldする。"""
    # TODO
    raise NotImplementedError


def iter_positive(values: Iterable[int]) -> Iterator[int]:
    """正の値だけyieldする。"""
    # TODO
    raise NotImplementedError


def sum_iterable(values: Iterable[int]) -> int:
    """iterableを受け取って合計する。"""
    # TODO
    raise NotImplementedError
