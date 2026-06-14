from importlib import import_module

target = import_module("exercises.rag_citation_verification.01_citations")


def test_cited_ids() -> None:
    assert target.cited_ids("答えです [source:chunk-1] [source:chunk-2]") == ["chunk-1", "chunk-2"]


def test_has_valid_citations() -> None:
    assert target.has_valid_citations("A [source:c1]", {"c1"}) is True
    assert target.has_valid_citations("A [source:c2]", {"c1"}) is False
    assert target.has_valid_citations("A", {"c1"}) is False


def test_answerable() -> None:
    assert target.answerable("根拠あり [source:c1]", {"c1"}) is True
    assert target.answerable("わかりません", {"c1"}) is False
