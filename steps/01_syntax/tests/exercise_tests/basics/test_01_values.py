from importlib import import_module

values = import_module("exercises.basics.01_values")


def test_make_profile() -> None:
    assert values.make_profile("Aki", 20) == "Aki is 20 years old"


def test_yen_to_text() -> None:
    assert values.yen_to_text(1200) == "1200円"


def test_minutes_to_seconds() -> None:
    assert values.minutes_to_seconds(3) == 180


def test_add_tax() -> None:
    assert values.add_tax(100, 0.1) == 110
