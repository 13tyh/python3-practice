"""RAG の検索部分を単純化して練習。"""


def tokenize(text: str) -> set[str]:
    # TODO
    raise NotImplementedError


def similarity(query: str, document: str) -> float:
    """Jaccard similarity。"""
    # TODO
    raise NotImplementedError


def retrieve(query: str, documents: list[str], top_k: int) -> list[str]:
    # TODO
    raise NotImplementedError


def chunk_text(text: str, max_chars: int) -> list[str]:
    # TODO
    raise NotImplementedError
