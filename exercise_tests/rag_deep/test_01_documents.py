from importlib import import_module

target = import_module("exercises.rag_deep.01_documents")


def test_documents() -> None:
    assert target.split_with_overlap("abcdef", chunk_size=3, overlap=1) == ["abc", "cde", "ef"]
    doc = target.Document("doc1", "abcdef", "manual.md")
    chunks = target.chunk_document(doc, 3, 1)
    assert chunks == [
        target.Chunk("doc1-0", "doc1", "abc", "manual.md", 0),
        target.Chunk("doc1-1", "doc1", "cde", "manual.md", 1),
        target.Chunk("doc1-2", "doc1", "ef", "manual.md", 2),
    ]

