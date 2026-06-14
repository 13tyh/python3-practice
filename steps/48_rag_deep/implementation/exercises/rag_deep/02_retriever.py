"""RAG retriever の練習。"""

from __future__ import annotations

from importlib import import_module

Chunk = import_module("exercises.rag_deep.01_documents").Chunk


def tokenize(text: str) -> set[str]:
    # TODO
    raise NotImplementedError


def score(query: str, chunk: Chunk) -> float:
    # TODO
    raise NotImplementedError


def retrieve(
    query: str,
    chunks: list[Chunk],
    top_k: int,
    min_score: float = 0,
) -> list[tuple[Chunk, float]]:
    # TODO
    raise NotImplementedError


def build_context(results: list[tuple[Chunk, float]]) -> str:
    # TODO
    raise NotImplementedError
