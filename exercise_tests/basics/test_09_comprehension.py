from importlib import import_module

target = import_module("exercises.basics.09_comprehension")


def test_square_numbers() -> None:
    assert target.square_numbers([2, 3]) == [4, 9]


def test_filter_positive() -> None:
    assert target.filter_positive([-1, 0, 2]) == [2]


def test_name_to_length() -> None:
    assert target.name_to_length(["Aki", "Ren"]) == {"Aki": 3, "Ren": 3}


def test_unique_sorted() -> None:
    assert target.unique_sorted([3, 1, 3, 2]) == [1, 2, 3]

