"""基礎反復 round 12."""

from collections.abc import Callable


def apply_all(value: str, funcs: list[Callable[[str], str]]) -> str:
    # TODO
    raise NotImplementedError


def make_prefixer(prefix: str) -> Callable[[str], str]:
    # TODO
    raise NotImplementedError


def fallback(func: Callable[[], str], default: str) -> str:
    # TODO
    raise NotImplementedError
