import pytest

from exercises.basics_repetition.round_19 import divide_or_raise, get_index, require_email


def test_round_19() -> None:
    assert require_email("aki@example.com") == "aki@example.com"
    with pytest.raises(ValueError):
        require_email("invalid")
    assert divide_or_raise(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        divide_or_raise(10, 0)
    assert get_index(["a"], 0) == "a"
    with pytest.raises(IndexError):
        get_index(["a"], 1)

