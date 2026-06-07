from importlib import import_module

target = import_module("exercises.basics.27_iterators")


def test_iterator_tasks() -> None:
    assert list(target.count_up_to(3)) == [1, 2, 3]
    assert list(target.take_even([1, 2, 3, 4])) == [2, 4]
    assert target.flatten([["a"], ["b", "c"]]) == ["a", "b", "c"]
    assert list(target.chunked([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
