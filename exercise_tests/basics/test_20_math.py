from importlib import import_module

target = import_module("exercises.basics.20_math")


def test_math_tasks() -> None:
    assert target.average([10, 20, 30]) == 20
    assert target.average([]) == 0.0
    assert target.clamp(12, 0, 10) == 10
    assert target.clamp(-1, 0, 10) == 0
    assert target.clamp(5, 0, 10) == 5
    assert target.percentage(25, 100) == 25.0
    assert target.percentage(1, 0) == 0.0
    assert target.round_price(12.6) == 13

