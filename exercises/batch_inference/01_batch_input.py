"""バッチ推論の入力データ作成。"""

from __future__ import annotations

import json
from pathlib import Path


def build_prompt_record(record_id: str, prompt: str) -> dict[str, object]:
    """1件分の推論入力を作る。"""
    # TODO
    raise NotImplementedError


def to_jsonl(records: list[dict[str, object]]) -> str:
    """list[dict] を JSONL 文字列にする。"""
    # TODO
    raise NotImplementedError


def write_jsonl(path: Path, records: list[dict[str, object]]) -> None:
    """UTF-8 で JSONL を書く。"""
    # TODO
    raise NotImplementedError


def read_jsonl(path: Path) -> list[dict[str, object]]:
    """JSONL を読む。"""
    # TODO
    raise NotImplementedError

