from importlib import import_module

target = import_module("exercises.embedding_metadata.01_chunks")


def test_build_chunk_id() -> None:
    assert target.build_chunk_id("doc-1", 2) == "doc-1:chunk:2"


def test_attach_metadata() -> None:
    assert target.attach_metadata(" body ", "doc-1", 0, "manual.pdf") == {
        "id": "doc-1:chunk:0",
        "text": "body",
        "metadata": {"document_id": "doc-1", "chunk_index": 0, "source": "manual.pdf"},
    }
    assert target.attach_metadata(" ", "doc-1", 0, "manual.pdf") is None


def test_valid_chunks() -> None:
    assert target.valid_chunks([{"text": "a"}, {"text": ""}, {"text": " "}]) == [{"text": "a"}]
