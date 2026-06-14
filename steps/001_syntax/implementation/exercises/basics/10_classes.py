"""class / dataclass の練習。"""

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    price: int


def total_price(books: list[Book]) -> int:
    # TODO
    raise NotImplementedError


class Counter:
    def __init__(self) -> None:
        # TODO
        raise NotImplementedError

    def increment(self) -> None:
        # TODO
        raise NotImplementedError

    def get(self) -> int:
        # TODO
        raise NotImplementedError
