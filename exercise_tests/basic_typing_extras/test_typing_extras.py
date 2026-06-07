from importlib import import_module

import pytest

target = import_module("exercises.basic_typing_extras.01_typing_extras")


def test_parse_role() -> None:
    assert target.parse_role("admin") == "admin"
    assert target.parse_role("unknown") == "viewer"
    assert target.parse_role(None) == "viewer"


def test_normalize_user_id() -> None:
    assert target.normalize_user_id(" u1 ") == "u1"
    with pytest.raises(ValueError):
        target.normalize_user_id(" ")


def test_as_string_list() -> None:
    assert target.as_string_list(["a", "b"]) == ["a", "b"]
    with pytest.raises(TypeError):
        target.as_string_list(["a", 1])


def test_cast_does_not_validate() -> None:
    assert target.unsafe_cast_example([1]) == [1]
