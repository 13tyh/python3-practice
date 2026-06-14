from importlib import import_module

import pytest

target = import_module("exercises.core_design_thinking.06_fail_fast")


def test_fail_fast() -> None:
    target.require_fields({"id": 1, "name": "Aki"}, ["id", "name"])
    with pytest.raises(ValueError):
        target.require_fields({"id": 1}, ["id", "name"])
    assert target.require_allowed("admin", {"admin", "member"}) == "admin"
    with pytest.raises(ValueError):
        target.require_allowed("owner", {"admin", "member"})
    assert target.parse_positive_int("10") == 10
    with pytest.raises(ValueError):
        target.parse_positive_int("0")
