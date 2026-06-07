"""ドキュメント分割の練習。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DocChunk:
    title: str
    body: str


def split_markdown_by_heading(text: str) -> list[DocChunk]:
    """Markdown を H1 見出しごとに分割する。"""
    # TODO
    raise NotImplementedError


def split_text_by_chars(text: str, max_chars: int) -> list[str]:
    """max_chars ごとに分割する。"""
    # TODO
    raise NotImplementedError


def safe_filename(title: str) -> str:
    """ファイル名に使いにくい文字を _ にする。"""
    # TODO
    raise NotImplementedError
