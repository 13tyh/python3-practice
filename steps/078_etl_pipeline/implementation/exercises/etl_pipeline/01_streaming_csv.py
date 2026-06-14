"""CSV行をstream処理するETL練習。"""

from collections.abc import Iterable, Iterator


def iter_valid_rows(rows: Iterable[dict[str, str]]) -> Iterator[dict[str, str]]:
    """topicがあり、minutesが正の整数の行だけyieldする。"""
    # TODO
    raise NotImplementedError


def summarize_minutes(rows: Iterable[dict[str, str]]) -> dict[str, int]:
    """有効行だけをtopicごとに合計する。"""
    # TODO
    raise NotImplementedError
