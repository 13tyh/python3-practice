from exercises.basics_repetition.round_01 import (
    clean_name,
    find_by_id,
    is_adult,
    only_even,
    price_with_tax,
)


def test_round_01() -> None:
    assert clean_name("  tanaka TARO ") == "Tanaka Taro"
    assert price_with_tax(1000) == 1100
    assert is_adult(18)
    assert not is_adult(17)
    assert only_even([1, 2, 3, 4]) == [2, 4]
    items = [{"id": "a", "name": "Aki"}]
    assert find_by_id(items, "a") == {"id": "a", "name": "Aki"}
    assert find_by_id(items, "x") is None

