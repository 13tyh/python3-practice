"""基礎反復 round 20."""

from dataclasses import dataclass


@dataclass
class Counter:
    value: int = 0


def increment(counter: Counter, step: int = 1) -> None:
    # TODO
    raise NotImplementedError


def reset(counter: Counter) -> None:
    # TODO
    raise NotImplementedError


def counter_label(counter: Counter) -> str:
    # TODO
    raise NotImplementedError
