"""RAG citation verificationの練習。"""


def cited_ids(answer: str) -> list[str]:
    """`[source:chunk-1]` 形式のcitation idを返す。"""
    # TODO
    raise NotImplementedError


def has_valid_citations(answer: str, valid_chunk_ids: set[str]) -> bool:
    """citationがあり、すべてvalidならTrue。"""
    # TODO
    raise NotImplementedError


def answerable(answer: str, valid_chunk_ids: set[str]) -> bool:
    """根拠あり回答ならTrue。"""
    # TODO
    raise NotImplementedError
