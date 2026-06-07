from exercises.basics_repetition.round_40 import get_name, get_or_guest, has_key, keys_list, set_role


def test_round_40() -> None:
    assert get_name({"name": "Aki"}) == "Aki"
    assert get_or_guest({"name": "Aki"}) == "Aki"
    assert get_or_guest({}) == "Guest"
    user = {"name": "Aki"}
    assert set_role(user, "admin") == {"name": "Aki", "role": "admin"}
    assert user == {"name": "Aki"}
    assert has_key({"a": "1"}, "a")
    assert keys_list({"b": "2", "a": "1"}) == ["a", "b"]

