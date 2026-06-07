from importlib import import_module

target = import_module("exercises.typing_deep.01_type_basics")


def test_type_basics() -> None:
    assert target.get_display_name(None) == "Guest"
    assert target.get_display_name("Aki") == "Aki"
    assert target.filter_names(["Aki", None, "", "Ren"]) == ["Aki", "Ren"]
    assert target.count_statuses(["active", "active", "deleted"]) == {
        "active": 2,
        "inactive": 0,
        "deleted": 1,
    }
    assert target.user_label({"id": "u1", "name": "Aki", "age": 20}) == "u1:Aki(20)"

