from importlib import import_module

target = import_module("exercises.basic_algorithms.01_algorithms")


def test_linear_search() -> None:
    assert target.linear_search(["a", "b"], "b") == 1
    assert target.linear_search(["a", "b"], "x") == -1


def test_binary_search() -> None:
    assert target.binary_search([1, 3, 5, 7], 5) == 2
    assert target.binary_search([1, 3, 5, 7], 2) == -1


def test_dedupe_keep_order() -> None:
    assert target.dedupe_keep_order(["a", "b", "a", "c"]) == ["a", "b", "c"]


def test_top_n_by_score() -> None:
    scores = {"b": 10, "a": 10, "c": 3}

    assert target.top_n_by_score(scores, 2) == ["a", "b"]
