from importlib import import_module

target = import_module("exercises.basics.19_tuple_set")


def test_tuple_set_tasks() -> None:
    assert target.to_point(1, 2) == (1, 2)
    assert target.swap_pair(("a", "b")) == ("b", "a")
    assert target.unique_names(["Aki", "Ren", "Aki"]) == {"Aki", "Ren"}
    assert target.common_items({"a", "b"}, {"b", "c"}) == {"b"}
    assert target.difference_items({"a", "b"}, {"b", "c"}) == {"a"}
