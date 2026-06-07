"""embedding用chunk metadataの練習。"""


def build_chunk_id(document_id: str, index: int) -> str:
    """安定したchunk idを返す。"""
    # TODO
    raise NotImplementedError


def attach_metadata(
    text: str, document_id: str, index: int, source: str
) -> dict[str, object] | None:
    """空textはNone、本文とmetadataを含むdictを返す。"""
    # TODO
    raise NotImplementedError


def valid_chunks(chunks: list[dict[str, object]]) -> list[dict[str, object]]:
    """textが空でないchunkだけ返す。"""
    # TODO
    raise NotImplementedError
