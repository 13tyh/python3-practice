from importlib import import_module

target = import_module("exercises.basics.05_list_dict")

users = [
    {"id": "u1", "name": "Aki", "role": "admin"},
    {"id": "u2", "name": "Ren", "role": "member"},
    {"id": "u3", "name": "Mio", "role": "member"},
]


def test_get_names() -> None:
    assert target.get_names(users) == ["Aki", "Ren", "Mio"]


def test_find_user() -> None:
    assert target.find_user(users, "u2") == users[1]
    assert target.find_user(users, "none") is None


def test_count_by_role() -> None:
    assert target.count_by_role(users) == {"admin": 1, "member": 2}


def test_merge_stock() -> None:
    current = {"pen": 3}
    result = target.merge_stock(current, {"pen": 2, "book": 1})
    assert result == {"pen": 5, "book": 1}
    assert current == {"pen": 3}
