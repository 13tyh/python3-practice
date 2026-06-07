"""パフォーマンスレビュー観点。"""


def has_db_call_in_loop(code_lines: list[str]) -> bool:
    """かなり単純な検出。for の後に repo. / db. があれば True。"""
    # TODO
    raise NotImplementedError


def estimate_n_plus_one_queries(parent_count: int) -> int:
    """親一覧1回 + 子取得N回。"""
    # TODO
    raise NotImplementedError


def is_better_query_count(before: int, after: int) -> bool:
    # TODO
    raise NotImplementedError

