"""performance の基礎。"""

from collections.abc import Iterator


def iter_csv_lines(lines: list[str]) -> Iterator[list[str]]:
    # TODO
    raise NotImplementedError


def chunk_items(items: list[int], size: int) -> Iterator[list[int]]:
    # TODO
    raise NotImplementedError


def measure_elapsed(func) -> tuple[object, float]:
    # TODO
    raise NotImplementedError
