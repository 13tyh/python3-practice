from importlib import import_module

import pytest

target = import_module("exercises.advanced.03_errors")


def test_require_non_empty() -> None:
    assert target.require_non_empty(" Aki ", "name") == "Aki"
    with pytest.raises(target.ValidationError):
        target.require_non_empty(" ", "name")


def test_find_required() -> None:
    assert target.find_required({"id": "1"}, "id") == "1"
    with pytest.raises(target.NotFoundError):
        target.find_required({}, "id")
