from exercises.basics_repetition.round_17 import (
    find_missing_keys,
    group_by_initial,
    invert_dict,
    sum_nested_amounts,
)


def test_round_17() -> None:
    assert group_by_initial(["Aki", "Ren", "Alice"]) == {"A": ["Aki", "Alice"], "R": ["Ren"]}
    assert invert_dict({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}
    assert sum_nested_amounts({"book": [100, 200], "pen": [50]}) == {"book": 300, "pen": 50}
    assert find_missing_keys({"id": "1"}, ["id", "name"]) == ["name"]

