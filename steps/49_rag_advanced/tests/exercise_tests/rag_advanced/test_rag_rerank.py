from importlib import import_module

target = import_module("exercises.rag_advanced.01_rag_rerank")


def test_rag_advanced() -> None:
    chunks = [{"text": "a", "source": "docs"}, {"text": "b", "source": "blog"}]
    assert target.metadata_filter(chunks, {"source": "docs"}) == [{"text": "a", "source": "docs"}]
    assert target.hybrid_score(0.5, 1.0, 0.2) == 0.9
    results = [{"id": "a", "score": 0.1}, {"id": "b", "score": 0.9}]
    assert target.rerank(results) == [{"id": "b", "score": 0.9}, {"id": "a", "score": 0.1}]
    assert target.is_grounded("Python FastAPI", "FastAPI is a Python framework")
    assert not target.is_grounded("Django", "FastAPI is a Python framework")
