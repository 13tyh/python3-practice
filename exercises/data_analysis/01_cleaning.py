"""データクリーニングの練習。"""


def remove_empty_rows(rows: list[dict[str, str | None]]) -> list[dict[str, str | None]]:
    # TODO
    raise NotImplementedError


def fill_missing(rows: list[dict[str, str | None]], key: str, default: str) -> list[dict[str, str]]:
    # TODO
    raise NotImplementedError


def deduplicate_by_key(rows: list[dict[str, str]], key: str) -> list[dict[str, str]]:
    # TODO
    raise NotImplementedError


def to_int(value: str | None, default: int = 0) -> int:
    # TODO
    raise NotImplementedError

