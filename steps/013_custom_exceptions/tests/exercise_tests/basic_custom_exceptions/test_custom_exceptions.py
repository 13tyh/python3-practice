from importlib import import_module

import pytest

target = import_module("exercises.basic_custom_exceptions.01_custom_exceptions")


def test_validate_age() -> None:
    assert target.validate_age(20) == 20

    with pytest.raises(target.ValidationError):
        target.validate_age(-1)


def test_safe_error_message() -> None:
    assert target.safe_error_message(target.ValidationError("bad age")) == "入力が正しくありません"
    assert target.safe_error_message(RuntimeError("secret token")) == "内部エラーが発生しました"
