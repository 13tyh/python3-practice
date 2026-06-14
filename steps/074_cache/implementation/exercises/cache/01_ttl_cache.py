"""TTL cache の基礎。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CacheItem:
    value: str
    expires_at: int


def build_cache_key(prefix: str, parts: list[str]) -> str:
    # TODO
    raise NotImplementedError


def get_cached(cache: dict[str, CacheItem], key: str, now: int) -> str | None:
    # TODO
    raise NotImplementedError


def set_cached(cache: dict[str, CacheItem], key: str, value: str, now: int, ttl: int) -> None:
    # TODO
    raise NotImplementedError
