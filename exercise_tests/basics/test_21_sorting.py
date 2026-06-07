from importlib import import_module

target = import_module("exercises.basics.21_sorting")


def test_sorting_tasks() -> None:
    numbers = [3, 1, 2]
    assert target.sort_numbers(numbers) == [1, 2, 3]
    assert numbers == [3, 1, 2]
    assert target.sort_names_ignore_case(["bob", "Aki", "ren"]) == ["Aki", "bob", "ren"]
    assert target.top_scores({"Aki": 90, "Ren": 70, "Mio": 80}, 2) == [("Aki", 90), ("Mio", 80)]
    users = [{"name": "Aki", "age": 30}, {"name": "Ren", "age": 20}]
    assert target.sort_users_by_age(users) == [{"name": "Ren", "age": 20}, {"name": "Aki", "age": 30}]

