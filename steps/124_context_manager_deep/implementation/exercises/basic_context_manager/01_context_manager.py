"""context managerの基礎練習。"""

from collections.abc import Iterator
from contextlib import contextmanager


class TimerLog:
    """withを抜けたらeventsに終了messageを追加する。"""

    def __init__(self, events: list[str], label: str) -> None:
        self.events = events
        self.label = label

    def __enter__(self) -> "TimerLog":
        # TODO
        raise NotImplementedError

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> bool:
        # TODO
        raise NotImplementedError


@contextmanager
def temporary_setting(settings: dict[str, str], key: str, value: str) -> Iterator[None]:
    """with内だけsettings[key]をvalueにする。"""
    # TODO
    raise NotImplementedError


def write_lines(path: str, lines: list[str]) -> None:
    """with openで行を書き込む。"""
    # TODO
    raise NotImplementedError
