from importlib import import_module

import pytest

vector = import_module("exercises.vector_search.01_vector_search")


def test_cosine_similarity() -> None:
    assert vector.cosine_similarity([1, 0], [1, 0]) == pytest.approx(1.0)
    assert vector.cosine_similarity([1, 0], [0, 1]) == pytest.approx(0.0)


def test_cosine_similarity_rejects_invalid_vectors() -> None:
    with pytest.raises(ValueError):
        vector.cosine_similarity([1, 2], [1])

    with pytest.raises(ValueError):
        vector.cosine_similarity([0, 0], [1, 1])


def test_top_k_returns_sorted_results() -> None:
    documents = [
        {"id": "b", "vector": [0.8, 0.2]},
        {"id": "a", "vector": [1.0, 0.0]},
        {"id": "c", "vector": [0.0, 1.0]},
    ]

    assert vector.top_k([1.0, 0.0], documents, k=2) == [
        {"id": "a", "score": pytest.approx(1.0)},
        {"id": "b", "score": pytest.approx(0.9701425)},
    ]
