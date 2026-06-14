from importlib import import_module

target = import_module("exercises.rag_deep.05_citations")


def test_citations() -> None:
    context = "[source: a.md]\nA\n[source: b.md]\nB"
    assert target.extract_sources(context) == ["a.md", "b.md"]
    assert target.append_citations("answer", ["a.md", "b.md"]) == "answer\n\nSources: a.md, b.md"
    assert target.citation_coverage("answer [source: a.md]", {"a.md", "b.md"}) == 0.5
