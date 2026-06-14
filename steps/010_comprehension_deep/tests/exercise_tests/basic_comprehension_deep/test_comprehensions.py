from importlib import import_module

target = import_module("exercises.basic_comprehension_deep.01_comprehensions")


def test_doubled_evens() -> None:
    assert target.doubled_evens([1, 2, 3, 4]) == [4, 8]


def test_users_by_id() -> None:
    users = [{"id": "u1", "name": "Aki"}, {"id": "u2", "name": "Ren"}]

    assert target.users_by_id(users) == {"u1": users[0], "u2": users[1]}


def test_normalized_tag_set() -> None:
    assert target.normalized_tag_set([" Python ", "python", "", "API"]) == {"python", "api"}
