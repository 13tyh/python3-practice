from importlib import import_module

target = import_module("exercises.basic_itertools_functools.01_iter_tools")


def test_group_sorted_pairs() -> None:
    pairs = [("b", 3), ("a", 1), ("a", 2)]

    assert target.group_sorted_pairs(pairs) == {"a": [1, 2], "b": [3]}


def test_make_multiplier() -> None:
    double = target.make_multiplier(2)

    assert double(5) == 10


def test_fibonacci() -> None:
    assert target.fibonacci(0) == 0
    assert target.fibonacci(1) == 1
    assert target.fibonacci(7) == 13


def test_flatten() -> None:
    assert target.flatten([["a", "b"], ["c"]]) == ["a", "b", "c"]
