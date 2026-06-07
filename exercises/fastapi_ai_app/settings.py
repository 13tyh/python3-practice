"""FastAPI AI app settings."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AISettings:
    provider: str
    model: str
    timeout_seconds: int


def load_ai_settings() -> AISettings:
    # TODO
    raise NotImplementedError


def validate_ai_settings(settings: AISettings) -> list[str]:
    # TODO
    raise NotImplementedError
