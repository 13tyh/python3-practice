"""asyncio の基礎練習。"""

from __future__ import annotations

import asyncio


async def async_double(number: int) -> int:
    # TODO
    raise NotImplementedError


async def double_all(numbers: list[int]) -> list[int]:
    """asyncio.gather を使って全部2倍にする。"""
    # TODO
    raise NotImplementedError


async def run_with_timeout(delay: float, timeout: float) -> str:
    """delay秒待つ処理をtimeout付きで実行する。時間内ならdone、超えたらtimeout。"""
    # TODO
    raise NotImplementedError


async def collect_in_order(values: list[str]) -> list[str]:
    """非同期関数で処理しても、入力順に返す。"""
    # TODO
    raise NotImplementedError


async def _sleep_and_return(value: str) -> str:
    await asyncio.sleep(0)
    return value

