"""RAG advanced の練習。"""


def metadata_filter(
    chunks: list[dict[str, object]],
    metadata: dict[str, str],
) -> list[dict[str, object]]:
    # TODO
    raise NotImplementedError


def hybrid_score(keyword_score: float, vector_score: float, alpha: float) -> float:
    # TODO
    raise NotImplementedError


def rerank(results: list[dict[str, object]]) -> list[dict[str, object]]:
    # TODO
    raise NotImplementedError


def is_grounded(answer: str, context: str) -> bool:
    # TODO
    raise NotImplementedError
