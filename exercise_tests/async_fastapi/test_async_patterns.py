import asyncio
from importlib import import_module

target = import_module("exercises.async_fastapi.01_async_patterns")


def test_async_patterns() -> None:
    assert asyncio.run(target.fetch_one("a")) == "fetched:a"
    assert asyncio.run(target.fetch_all(["a", "b"])) == ["fetched:a", "fetched:b"]

    async def collect() -> list[str]:
        return [token async for token in target.stream_tokens("a b")]

    assert asyncio.run(collect()) == ["a", "b"]

