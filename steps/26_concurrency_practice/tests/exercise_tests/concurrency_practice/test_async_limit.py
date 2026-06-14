import asyncio
from importlib import import_module

target = import_module("exercises.concurrency_practice.01_async_limit")


def test_async_limit() -> None:
    assert asyncio.run(target.run_limited([1, 2, 3], 2)) == [2, 4, 6]
    assert asyncio.run(target.cancel_if_slow(0, 1)) == "done"
    assert asyncio.run(target.cancel_if_slow(0.05, 0.001)) == "timeout"
