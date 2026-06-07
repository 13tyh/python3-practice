from importlib import import_module

target = import_module("exercises.basics.12_mini_tasks")


def test_build_query() -> None:
    assert target.build_query({"name": "Aki", "role": "", "area": None}) == {"name": "Aki"}


def test_validate_user_input() -> None:
    assert target.validate_user_input({"name": "Aki", "email": "a@example.com"}) == []
    assert target.validate_user_input({"name": "", "email": ""}) == [
        "name is required",
        "email is required",
    ]


def test_calculate_cart() -> None:
    items = [{"price": 100, "quantity": 2}, {"price": 50, "quantity": 1}]
    assert target.calculate_cart(items) == {"subtotal": 250, "tax": 25, "total": 275}

