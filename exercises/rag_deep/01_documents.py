"""RAG document / chunk の練習。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    id: str
    text: str
    source: str


@dataclass(frozen=True)
class Chunk:
    id: str
    document_id: str
    text: str
    source: str
    index: int


def split_with_overlap(text: str, chunk_size: int, overlap: int) -> list[str]:
    # TODO
    raise NotImplementedError


def chunk_document(document: Document, chunk_size: int, overlap: int) -> list[Chunk]:
    # TODO
    raise NotImplementedError

