"""HTTP / API の基礎練習。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from urllib.parse import urlencode


@dataclass(frozen=True)
class ApiResult:
    status_code: int
    body: dict[str, Any]


def build_url(base_url: str, path: str, params: dict[str, str]) -> str:
    """base_url、path、query params からURLを作る。"""
    # TODO
    raise NotImplementedError


def build_auth_headers(api_key: str) -> dict[str, str]:
    """Bearer token の Authorization header を作る。"""
    # TODO
    raise NotImplementedError


def is_success(status_code: int) -> bool:
    """2xxならTrue。"""
    # TODO
    raise NotImplementedError


def extract_items(result: ApiResult) -> list[dict[str, Any]]:
    """body['items'] が list なら返す。なければ空 list。"""
    # TODO
    raise NotImplementedError


def safe_error_message(status_code: int, message: str) -> str:
    """ログ用に短いエラーメッセージを作る。"""
    # TODO
    raise NotImplementedError

