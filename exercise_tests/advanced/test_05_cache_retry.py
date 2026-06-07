from importlib import import_module

import pytest

target = import_module("exercises.advanced.05_cache_retry")


def test_memoize_upper() -> None:
    cache: dict[str, str] = {}
    assert target.memoize_upper("python", cache) == "PYTHON"
    assert cache == {"python": "PYTHON"}


def test_retry_call() -> None:
    count = {"value": 0}

    def flaky() -> str:
        count["value"] += 1
        if count["value"] < 2:
            raise RuntimeError("failed")
        return "ok"

    assert target.retry_call(flaky, retries=2) == "ok"

    with pytest.raises(RuntimeError):
        target.retry_call(lambda: (_ for _ in ()).throw(RuntimeError("ng")), retries=1)

