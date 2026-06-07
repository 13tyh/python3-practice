"""RAG 評価の練習。"""

from __future__ import annotations


def recall_at_k(retrieved_ids: list[str], expected_ids: set[str], k: int) -> float:
    # TODO
    raise NotImplementedError


def has_citation(answer: str) -> bool:
    """[source: xxx] のような引用があれば True。"""
    # TODO
    raise NotImplementedError


def should_answer(results_count: int, min_results: int = 1) -> bool:
    # TODO
    raise NotImplementedError

