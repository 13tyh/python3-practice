import asyncio
from importlib import import_module

target = import_module("exercises.async_python.01_asyncio_basics")


def test_async_double() -> None:
    assert asyncio.run(target.async_double(3)) == 6


def test_double_all() -> None:
    assert asyncio.run(target.double_all([1, 2, 3])) == [2, 4, 6]


def test_run_with_timeout() -> None:
    assert asyncio.run(target.run_with_timeout(0, 1)) == "done"
    assert asyncio.run(target.run_with_timeout(0.05, 0.001)) == "timeout"


def test_collect_in_order() -> None:
    assert asyncio.run(target.collect_in_order(["a", "b"])) == ["a", "b"]

