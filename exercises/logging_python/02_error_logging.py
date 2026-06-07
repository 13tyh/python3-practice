"""例外ログの練習。"""

from __future__ import annotations

import logging
from collections.abc import Callable


def run_with_error_log(logger: logging.Logger, action: str, func: Callable[[], str]) -> str | None:
    """func を実行し、例外時は logger.exception して None を返す。"""
    # TODO
    raise NotImplementedError


def should_log_debug(env: str) -> bool:
    """local/dev/test なら debug log を出してよい。"""
    # TODO
    raise NotImplementedError


def safe_log_message(message: str) -> str:
    """改行を空白にしてログ注入っぽい崩れを避ける。"""
    # TODO
    raise NotImplementedError

