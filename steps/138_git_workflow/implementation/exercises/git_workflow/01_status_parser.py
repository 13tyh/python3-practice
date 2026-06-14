"""git statusを読む練習。"""


def parse_short_status(lines: list[str]) -> dict[str, list[str]]:
    """` M file.py` や `?? file.py` を状態ごとに分類する。"""
    # TODO
    raise NotImplementedError


def branch_summary(line: str) -> dict[str, str | int]:
    """`## master...origin/master [ahead 1, behind 2]` をdictにする。"""
    # TODO
    raise NotImplementedError
