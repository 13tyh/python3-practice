"""asyncio semaphore / cancellation の練習。"""

import asyncio


async def limited_double(value: int, semaphore: asyncio.Semaphore) -> int:
    # TODO
    raise NotImplementedError


async def run_limited(values: list[int], limit: int) -> list[int]:
    # TODO
    raise NotImplementedError


async def cancel_if_slow(delay: float, timeout: float) -> str:
    # TODO
    raise NotImplementedError

