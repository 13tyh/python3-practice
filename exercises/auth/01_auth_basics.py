"""認証・認可の基礎。"""

from __future__ import annotations


def extract_bearer_token(header: str | None) -> str | None:
    # TODO
    raise NotImplementedError


def is_valid_api_key(api_key: str | None, allowed_keys: set[str]) -> bool:
    # TODO
    raise NotImplementedError


def has_permission(user_roles: list[str], required_role: str) -> bool:
    # TODO
    raise NotImplementedError


def mask_token(token: str | None) -> str:
    # TODO
    raise NotImplementedError
