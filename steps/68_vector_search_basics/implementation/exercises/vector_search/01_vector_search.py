"""RAGの前提になるvector searchを自力で書く練習。"""

from collections.abc import Sequence
from typing import TypedDict


class DocumentVector(TypedDict):
    id: str
    vector: list[float]


class SearchResult(TypedDict):
    id: str
    score: float


def cosine_similarity(left: Sequence[float], right: Sequence[float]) -> float:
    """2つのvectorのcosine similarityを返す。"""
    # TODO
    raise NotImplementedError


def top_k(query: Sequence[float], documents: list[DocumentVector], k: int) -> list[SearchResult]:
    """score降順で上位k件を返す。同点ならid昇順。"""
    # TODO
    raise NotImplementedError
