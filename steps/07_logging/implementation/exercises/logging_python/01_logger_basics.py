"""logging の基礎練習。"""

from __future__ import annotations

import logging


def get_logger(name: str) -> logging.Logger:
    """指定名の logger を返す。"""
    # TODO
    raise NotImplementedError


def parse_log_level(level: str) -> int:
    """文字列の level を logging の定数に変換する。不明なら INFO。"""
    # TODO
    raise NotImplementedError


def mask_value(value: str | None) -> str:
    """ログ用に secret を隠す。"""
    # TODO
    raise NotImplementedError


def build_log_context(user_id: str, action: str, status: str) -> dict[str, str]:
    """構造化ログ用の context を作る。"""
    # TODO
    raise NotImplementedError


def log_success(logger: logging.Logger, action: str, user_id: str) -> None:
    """成功ログを INFO で出す。"""
    # TODO
    raise NotImplementedError
