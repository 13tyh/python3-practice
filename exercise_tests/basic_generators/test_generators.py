from importlib import import_module

target = import_module("exercises.basic_generators.01_generators")


def test_count_up_to() -> None:
    assert list(target.count_up_to(3)) == [0, 1, 2]


def test_iter_positive() -> None:
    assert list(target.iter_positive([-1, 0, 2, 3])) == [2, 3]


def test_sum_iterable() -> None:
    assert target.sum_iterable(value for value in [1, 2, 3]) == 6
