from importlib import import_module

target = import_module("exercises.rag_basics.01_retrieval")


def test_rag_basics() -> None:
    assert target.tokenize("Python python API") == {"python", "api"}
    assert target.similarity("python api", "python fastapi") == 1 / 3
    docs = ["MongoDB aggregation", "FastAPI Python API", "CSS layout"]
    assert target.retrieve("python api", docs, top_k=2) == [
        "FastAPI Python API",
        "MongoDB aggregation",
    ]
    assert target.chunk_text("abcdef", 2) == ["ab", "cd", "ef"]
