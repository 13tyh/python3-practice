"""bulk / chunk 処理の練習。"""


def unique_ids(ids: list[str]) -> list[str]:
    """順序を保って重複削除。"""
    # TODO
    raise NotImplementedError


def chunked(items: list[str], size: int) -> list[list[str]]:
    # TODO
    raise NotImplementedError


def build_in_query(field: str, values: list[str]) -> dict[str, dict[str, list[str]]]:
    # TODO
    raise NotImplementedError


def avoid_full_scan_lookup(rows: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    """毎回 list scan しないため key -> row の辞書を作る。"""
    # TODO
    raise NotImplementedError

