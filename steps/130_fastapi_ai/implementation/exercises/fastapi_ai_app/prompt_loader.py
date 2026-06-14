"""Prompt template loader."""

from __future__ import annotations

from pathlib import Path


def load_prompt_template(path: Path) -> str:
    # TODO
    raise NotImplementedError


def render_prompt(template: str, values: dict[str, str]) -> str:
    # TODO
    raise NotImplementedError


def default_review_prompt_path() -> Path:
    return Path(__file__).parent / "prompts" / "review_prompt.md"
