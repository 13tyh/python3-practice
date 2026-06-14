"""特化型RAG設計の練習。"""


def chunk_size_for_document(document_type: str) -> int:
    """文書種別ごとのchunk sizeを返す。"""
    # TODO
    raise NotImplementedError


def needs_metadata_filter(query: str) -> bool:
    """city: や plan: を含むqueryならmetadata filterが必要。"""
    # TODO
    raise NotImplementedError


def rag_blueprint(document_type: str, requires_citation: bool) -> dict[str, object]:
    """RAG構成の概要を返す。"""
    # TODO
    raise NotImplementedError
