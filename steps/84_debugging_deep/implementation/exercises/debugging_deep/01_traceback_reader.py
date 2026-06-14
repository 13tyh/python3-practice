"""tracebackを読む練習。"""


def exception_name(traceback_text: str) -> str:
    """traceback末尾の例外名を返す。"""
    # TODO
    raise NotImplementedError


def last_file_line(traceback_text: str) -> tuple[str, int] | None:
    """最後に出てきた `File "...", line N` を返す。"""
    # TODO
    raise NotImplementedError


def investigation_note(traceback_text: str) -> str:
    """例外名と最後のfile/lineを含む調査メモを返す。"""
    # TODO
    raise NotImplementedError
