from importlib import import_module

target = import_module("exercises.rag_practice.01_rag_quality")


def test_rag_quality() -> None:
    assert target.is_answerable([0.2, 0.8], 0.7)
    assert not target.is_answerable([0.2], 0.7)
    assert target.require_citations("answer [source: docs.md]")
    assert target.rerank_by_score([("a", 0.1), ("b", 0.9)]) == [("b", 0.9), ("a", 0.1)]
    assert target.compare_chunk_sizes({200: 0.7, 500: 0.8}) == 500

