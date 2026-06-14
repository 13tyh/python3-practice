"""セキュリティ基礎チェック。"""

from __future__ import annotations

from pathlib import Path


def is_path_inside(base_dir: Path, target: Path) -> bool:
    # TODO
    raise NotImplementedError


def contains_prompt_injection(text: str) -> bool:
    # TODO
    raise NotImplementedError


def redact_secrets(text: str) -> str:
    # TODO
    raise NotImplementedError
