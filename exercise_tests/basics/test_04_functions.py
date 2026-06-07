from importlib import import_module

target = import_module("exercises.basics.04_functions")


def test_is_even() -> None:
    assert target.is_even(2)
    assert not target.is_even(3)


def test_is_valid_email() -> None:
    assert target.is_valid_email("a@example.com")
    assert not target.is_valid_email("a.example.com")


def test_apply_discount() -> None:
    assert target.apply_discount(1000, 0.2) == 800


def test_summarize_scores() -> None:
    assert target.summarize_scores([10, 30, 20]) == {"max": 30, "min": 10, "total": 60}
    assert target.summarize_scores([]) == {"max": 0, "min": 0, "total": 0}

