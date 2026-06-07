from exercises.basics_repetition.round_26 import (
    is_valid_age,
    normalize_phone,
    remove_empty_strings,
    user_initials,
)


def test_round_26() -> None:
    assert normalize_phone("090-1234-5678") == "09012345678"
    assert is_valid_age(0)
    assert is_valid_age(120)
    assert not is_valid_age(-1)
    assert user_initials("Tanaka Taro") == "TT"
    assert remove_empty_strings(["a", "", " ", "b"]) == ["a", "b"]

