"""JSONL ログ分析。"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def read_jsonl_logs(path: Path) -> list[dict[str, Any]]:
    # TODO
    raise NotImplementedError


def error_rate(logs: list[dict[str, Any]]) -> float:
    # TODO
    raise NotImplementedError


def average_elapsed_ms(logs: list[dict[str, Any]]) -> float:
    # TODO
    raise NotImplementedError


def count_by_action(logs: list[dict[str, Any]]) -> dict[str, int]:
    # TODO
    raise NotImplementedError
