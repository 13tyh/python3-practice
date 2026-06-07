from importlib import import_module

target = import_module("exercises.domain_rag_blueprint.01_blueprint")


def test_chunk_size_for_document() -> None:
    assert target.chunk_size_for_document("faq") == 400
    assert target.chunk_size_for_document("policy") == 800


def test_needs_metadata_filter() -> None:
    assert target.needs_metadata_filter("city:tokyo 契約") is True
    assert target.needs_metadata_filter("契約について") is False


def test_rag_blueprint() -> None:
    assert target.rag_blueprint("faq", True) == {
        "chunk_size": 400,
        "retriever": "hybrid",
        "rerank": True,
        "citation_required": True,
    }
