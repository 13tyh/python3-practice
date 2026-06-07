from importlib import import_module

target = import_module("exercises.basics.18_bool_none")


def test_bool_none_tasks() -> None:
    assert target.is_blank(None)
    assert target.is_blank("  ")
    assert not target.is_blank("x")
    assert target.default_if_none(None, "guest") == "guest"
    assert target.default_if_none("Aki", "guest") == "Aki"
    assert target.to_bool("YES")
    assert target.to_bool("on")
    assert not target.to_bool("no")
    assert target.all_present(["a", "b"])
    assert not target.all_present(["a", None])
    assert target.any_empty(["a", ""])
