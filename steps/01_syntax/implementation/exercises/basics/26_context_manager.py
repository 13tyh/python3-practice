"""with / context manager の練習。"""

from pathlib import Path


def read_first_line(path: Path) -> str:
    # TODO
    raise NotImplementedError


def write_and_read(path: Path, text: str) -> str:
    # TODO
    raise NotImplementedError


class SimpleResource:
    def __init__(self) -> None:
        self.opened = False

    def __enter__(self) -> "SimpleResource":
        # TODO
        raise NotImplementedError

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None:
        # TODO
        raise NotImplementedError
