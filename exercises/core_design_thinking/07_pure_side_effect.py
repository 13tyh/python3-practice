"""pure function と side effect 分離の練習。"""

from pathlib import Path


def build_report_text(rows: list[dict[str, str]]) -> str:
    # TODO
    raise NotImplementedError


def write_report(path: Path, text: str) -> None:
    # TODO
    raise NotImplementedError


def create_report(path: Path, rows: list[dict[str, str]]) -> None:
    # TODO
    raise NotImplementedError

