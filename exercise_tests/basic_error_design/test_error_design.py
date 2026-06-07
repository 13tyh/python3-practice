from importlib import import_module

import pytest

target = import_module("exercises.basic_error_design.01_error_design")


def test_classify_status_code() -> None:
    assert target.classify_status_code(200) == "success"
    assert target.classify_status_code(429) == "retryable"
    assert target.classify_status_code(500) == "retryable"
    assert target.classify_status_code(404) == "permanent"


def test_parse_positive_int() -> None:
    assert target.parse_positive_int("10") == 10
    with pytest.raises(ValueError):
        target.parse_positive_int("0")
    with pytest.raises(ValueError):
        target.parse_positive_int("abc")


def test_should_retry() -> None:
    assert target.should_retry(target.RetryableError()) is True
    assert target.should_retry(target.PermanentError()) is False
