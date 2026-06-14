import pytest

from exercises.basics_repetition.round_04 import (
    build_query,
    chunk,
    flatten,
    update_without_mutating,
    validate_positive,
)


def test_round_04() -> None:
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert flatten([["a"], ["b", "c"]]) == ["a", "b", "c"]
    data = {"a": 1}
    assert update_without_mutating(data, "b", 2) == {"a": 1, "b": 2}
    assert data == {"a": 1}
    assert validate_positive(1) == 1
    with pytest.raises(ValueError):
        validate_positive(0)
    assert build_query({"name": "Aki", "role": "", "area": None}) == {"name": "Aki"}
