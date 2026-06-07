from importlib import import_module

target = import_module("exercises.basics.13_slice")


def test_slice_tasks() -> None:
    assert target.first_item(["a", "b"]) == "a"
    assert target.first_item([]) is None
    assert target.last_item(["a", "b"]) == "b"
    assert target.last_item([]) is None
    assert target.first_three([1, 2, 3, 4]) == [1, 2, 3]
    assert target.reverse_text("abc") == "cba"
    assert target.every_second([1, 2, 3, 4, 5]) == [1, 3, 5]

