from dataclasses import FrozenInstanceError
from importlib import import_module

import pytest

target = import_module("exercises.basic_dataclass_deep.01_dataclass")


def test_create_user_is_frozen_and_uses_tuple_tags() -> None:
    user = target.create_user("u1", "sato", ["admin", "ai"])

    assert user.tags == ("admin", "ai")
    with pytest.raises(FrozenInstanceError):
        user.name = "changed"


def test_batch_result_lists_are_not_shared() -> None:
    first = target.BatchResult()
    second = target.BatchResult()
    target.add_success(first, "a")

    assert first.success_ids == ["a"]
    assert second.success_ids == []


def test_success_rate() -> None:
    result = target.BatchResult(success_ids=["a", "b"], failed_ids=["c"])

    assert target.success_rate(result) == pytest.approx(2 / 3)
    assert target.success_rate(target.BatchResult()) == 0.0
