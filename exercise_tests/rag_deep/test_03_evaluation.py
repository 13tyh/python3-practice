from importlib import import_module

target = import_module("exercises.rag_deep.03_evaluation")


def test_rag_evaluation() -> None:
    assert target.recall_at_k(["c1", "c2"], {"c2", "c3"}, 2) == 0.5
    assert target.has_citation("answer [source: manual.md]")
    assert not target.has_citation("answer only")
    assert target.should_answer(1)
    assert not target.should_answer(0)
