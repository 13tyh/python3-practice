from exercises.basics_repetition.round_39 import add_item, contains_item, count_items, first, last


def test_round_39() -> None:
    assert first(["a", "b"]) == "a"
    assert first([]) is None
    assert last(["a", "b"]) == "b"
    assert last([]) is None
    items = ["a"]
    assert add_item(items, "b") == ["a", "b"]
    assert items == ["a"]
    assert count_items(["a", "b"]) == 2
    assert contains_item(["a"], "a")

