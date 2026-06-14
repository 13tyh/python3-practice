from importlib import import_module

target = import_module("exercises.design_patterns.01_patterns")


def test_patterns() -> None:
    assert target.apply_strategy("Hello", target.UpperFormatter()) == "HELLO"
    assert target.apply_strategy("Hello", target.LowerFormatter()) == "hello"
    assert isinstance(target.formatter_factory("upper"), target.UpperFormatter)
    assert isinstance(target.formatter_factory("lower"), target.LowerFormatter)
