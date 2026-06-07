from importlib import import_module

target = import_module("exercises.basics.02_if")


def test_judge_age() -> None:
    assert target.judge_age(18) == "adult"
    assert target.judge_age(17) == "minor"


def test_max_number() -> None:
    assert target.max_number(3, 9) == 9


def test_shipping_fee() -> None:
    assert target.shipping_fee(4000, "東京") == 500
    assert target.shipping_fee(5000, "東京") == 0
    assert target.shipping_fee(5000, "北海道") == 500
    assert target.shipping_fee(8000, "沖縄") == 0


def test_password_strength() -> None:
    assert target.password_strength("abc") == "weak"
    assert target.password_strength("abcdefgh") == "normal"
    assert target.password_strength("abc12345") == "strong"

