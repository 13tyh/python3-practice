from importlib import import_module

target = import_module("exercises.rate_limiting.01_fixed_window")


def test_count_in_window() -> None:
    assert target.count_in_window([1, 5, 11], now=12, window_seconds=10) == 2


def test_is_allowed() -> None:
    assert target.is_allowed([1, 5], now=12, limit=3, window_seconds=10) is True
    assert target.is_allowed([3, 5, 11], now=12, limit=3, window_seconds=10) is False


def test_retry_after_seconds() -> None:
    assert target.retry_after_seconds([3, 5, 11], now=12, window_seconds=10) == 1
