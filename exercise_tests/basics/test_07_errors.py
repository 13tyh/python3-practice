from importlib import import_module

import pytest

target = import_module("exercises.basics.07_errors")


def test_safe_divide() -> None:
    assert target.safe_divide(10, 2) == 5
    assert target.safe_divide(10, 0) is None


def test_parse_int() -> None:
    assert target.parse_int("12") == 12
    with pytest.raises(ValueError):
        target.parse_int("x")


def test_require_positive() -> None:
    assert target.require_positive(1) == 1
    with pytest.raises(ValueError):
        target.require_positive(0)


def test_get_required() -> None:
    assert target.get_required({"name": "Aki"}, "name") == "Aki"
    with pytest.raises(KeyError):
        target.get_required({}, "name")

