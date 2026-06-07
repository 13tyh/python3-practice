from exercises.basics_repetition.round_51 import (
    all_tags,
    flatten_matrix,
    multiplication_table,
    pairs,
)


def test_round_51() -> None:
    assert flatten_matrix([[1, 2], [3]]) == [1, 2, 3]
    assert pairs(["a", "b"], ["1", "2"]) == [("a", "1"), ("a", "2"), ("b", "1"), ("b", "2")]
    assert multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    assert all_tags([{"tags": ["py", "api"]}, {"tags": ["db"]}]) == ["py", "api", "db"]
