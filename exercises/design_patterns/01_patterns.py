"""小さい設計パターン。"""

from typing import Protocol


class Formatter(Protocol):
    def format(self, text: str) -> str:
        """Format text."""


class UpperFormatter:
    def format(self, text: str) -> str:
        return text.upper()


class LowerFormatter:
    def format(self, text: str) -> str:
        return text.lower()


def formatter_factory(name: str) -> Formatter:
    # TODO
    raise NotImplementedError


def apply_strategy(text: str, formatter: Formatter) -> str:
    # TODO
    raise NotImplementedError

