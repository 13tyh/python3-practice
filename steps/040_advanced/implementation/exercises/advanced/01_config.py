"""設定読み込みの応用。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    env: str
    debug: bool
    mongo_uri: str


def load_config() -> AppConfig:
    # TODO
    raise NotImplementedError


def is_production(config: AppConfig) -> bool:
    # TODO
    raise NotImplementedError
