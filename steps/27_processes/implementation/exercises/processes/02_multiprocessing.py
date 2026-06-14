"""multiprocessing の練習。"""

from __future__ import annotations

from multiprocessing import Queue


def square(number: int) -> int:
    # TODO
    raise NotImplementedError


def square_all(numbers: list[int]) -> list[int]:
    """Poolを使って全て2乗する。"""
    # TODO
    raise NotImplementedError


def worker_put_square(number: int, queue: Queue[int]) -> None:
    """numberの2乗をqueueに入れる。"""
    # TODO
    raise NotImplementedError


def split_chunks(items: list[int], chunk_size: int) -> list[list[int]]:
    """chunk_sizeごとに分割する。"""
    # TODO
    raise NotImplementedError
