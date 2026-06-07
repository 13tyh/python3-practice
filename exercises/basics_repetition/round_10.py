"""基礎反復 round 10."""

from dataclasses import dataclass


@dataclass
class Todo:
    title: str
    done: bool = False


def complete(todo: Todo) -> None:
    # TODO
    raise NotImplementedError


def active_titles(todos: list[Todo]) -> list[str]:
    # TODO
    raise NotImplementedError


def completion_rate(todos: list[Todo]) -> float:
    # TODO
    raise NotImplementedError
