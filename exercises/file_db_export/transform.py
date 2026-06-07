"""DB document を CSV row に変換する練習。"""

from __future__ import annotations

from typing import Any


def normalize_value(value: Any) -> str:
    """CSV に書きやすい文字列へ変換する。None は空文字。"""
    # TODO
    raise NotImplementedError


def document_to_row(document: dict[str, Any], fields: list[str]) -> dict[str, str]:
    # TODO
    raise NotImplementedError


def documents_to_rows(documents: list[dict[str, Any]], fields: list[str]) -> list[dict[str, str]]:
    # TODO
    raise NotImplementedError
