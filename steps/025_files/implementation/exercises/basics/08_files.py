"""ファイル操作の練習。"""

from pathlib import Path


def write_lines(path: Path, lines: list[str]) -> None:
    """各要素を1行としてUTF-8で書く。"""
    # TODO
    raise NotImplementedError


def read_lines(path: Path) -> list[str]:
    """改行を除いて読む。"""
    # TODO
    raise NotImplementedError


def append_log(path: Path, message: str) -> None:
    """末尾にmessageを1行追加する。"""
    # TODO
    raise NotImplementedError


def count_lines(path: Path) -> int:
    # TODO
    raise NotImplementedError
