"""AI streaming の基礎。"""

from __future__ import annotations

from collections.abc import Iterator


def split_tokens(text: str) -> list[str]:
    # TODO
    raise NotImplementedError


def stream_text(text: str) -> Iterator[str]:
    # TODO
    raise NotImplementedError


def to_sse_event(token: str) -> str:
    # TODO
    raise NotImplementedError

