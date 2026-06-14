"""巨大ファイルを想定したline stream処理の練習。"""

from collections.abc import Iterable, Iterator


def iter_effective_lines(lines: Iterable[str]) -> Iterator[str]:
    """空行と#コメント行を除き、strip済みの行をyieldする。"""
    # TODO
    raise NotImplementedError


def count_prefix(lines: Iterable[str], prefix: str) -> int:
    """有効行のうちprefixで始まる行数を数える。"""
    # TODO
    raise NotImplementedError
