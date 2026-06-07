from exercises.basics_repetition.round_34 import (
    frequency_sorted,
    intersection_preserve_order,
    unique_preserve_order,
)


def test_round_34() -> None:
    assert unique_preserve_order(["a", "b", "a", "c"]) == ["a", "b", "c"]
    assert intersection_preserve_order(["a", "b", "c"], ["c", "a"]) == ["a", "c"]
    assert frequency_sorted(["b", "a", "b", "c", "a", "b"]) == [("b", 3), ("a", 2), ("c", 1)]
