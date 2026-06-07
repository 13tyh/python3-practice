from exercises.basics_repetition.round_55 import (
    clean_and_filter,
    for_to_comprehension_dict,
    for_to_comprehension_numbers,
    nested_filter,
)


def test_round_55() -> None:
    assert for_to_comprehension_numbers([1, 2, 3, 4]) == [4, 8]
    items = [{"id": "u1", "name": "Aki"}, {"id": "u2", "name": "Ren"}]
    assert for_to_comprehension_dict(items) == {"u1": "Aki", "u2": "Ren"}
    assert nested_filter([[1, -1], [0, 2]]) == [1, 2]
    assert clean_and_filter([" A ", "", " b "]) == ["a", "b"]
