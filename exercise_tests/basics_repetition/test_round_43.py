from exercises.basics_repetition.round_43 import (
    is_missing,
    list_or_empty,
    name_or_guest,
    value_or_default,
)


def test_round_43() -> None:
    assert value_or_default(None, 10) == 10
    assert value_or_default(0, 10) == 0
    assert name_or_guest(None) == "Guest"
    assert name_or_guest("") == "Guest"
    assert name_or_guest("Aki") == "Aki"
    assert list_or_empty(None) == []
    assert list_or_empty(["a"]) == ["a"]
    assert is_missing(None)
    assert not is_missing("")
