from importlib import import_module

docs = import_module("exercises.rag_deep.01_documents")
target = import_module("exercises.rag_deep.02_retriever")


def test_retriever() -> None:
    chunks = [
        docs.Chunk("c1", "d1", "python fastapi api", "a.md", 0),
        docs.Chunk("c2", "d2", "mongo aggregation pipeline", "b.md", 0),
    ]
    assert target.tokenize("Python API") == {"python", "api"}
    assert target.score("python api", chunks[0]) == 2 / 3
    results = target.retrieve("python api", chunks, top_k=1)
    assert results[0][0].id == "c1"
    assert target.build_context(results) == "[source: a.md]\npython fastapi api"

