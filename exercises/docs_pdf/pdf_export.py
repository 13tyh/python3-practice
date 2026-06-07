"""PDF 出力の練習。"""

from __future__ import annotations

from pathlib import Path

from .split_docs import DocChunk


def chunk_to_text(chunk: DocChunk) -> str:
    # TODO
    raise NotImplementedError


def write_text_pdf(path: Path, title: str, lines: list[str]) -> None:
    """reportlab で簡単な PDF を作る。"""
    # TODO
    raise NotImplementedError


def build_output_paths(output_dir: Path, chunks: list[DocChunk]) -> list[Path]:
    # TODO
    raise NotImplementedError

