from importlib import import_module

target = import_module("exercises.basic_list_methods.01_list_methods")


def test_append_item_does_not_mutate_original() -> None:
    values = ["a"]

    assert target.append_item(values, "b") == ["a", "b"]
    assert values == ["a"]


def test_first_or_none() -> None:
    assert target.first_or_none(["a", "b"]) == "a"
    assert target.first_or_none([]) is None


def test_extend_items() -> None:
    assert target.extend_items(["a"], ["b", "c"]) == ["a", "b", "c"]
