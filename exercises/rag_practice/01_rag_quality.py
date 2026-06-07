"""RAG 実践評価。"""


def is_answerable(scores: list[float], threshold: float) -> bool:
    # TODO
    raise NotImplementedError


def require_citations(answer: str) -> bool:
    # TODO
    raise NotImplementedError


def rerank_by_score(results: list[tuple[str, float]]) -> list[tuple[str, float]]:
    # TODO
    raise NotImplementedError


def compare_chunk_sizes(metrics: dict[int, float]) -> int:
    """score が一番高い chunk size を返す。"""
    # TODO
    raise NotImplementedError
