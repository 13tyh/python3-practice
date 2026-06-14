"""async FastAPI で使う考え方。"""

from __future__ import annotations

from collections.abc import AsyncIterator


async def fetch_one(value: str) -> str:
    # TODO
    raise NotImplementedError


async def fetch_all(values: list[str]) -> list[str]:
    # TODO
    raise NotImplementedError


async def stream_tokens(text: str) -> AsyncIterator[str]:
    # TODO
    raise NotImplementedError
