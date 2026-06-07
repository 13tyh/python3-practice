from importlib import import_module

target = import_module("exercises.refactoring.01_refactor_targets")


def test_refactoring() -> None:
    item = {"price": 100, "quantity": 3}
    assert target.item_total(item) == 300
    assert target.apply_discount(1000, 0.2) == 800
    assert target.calculate_tax(1000) == 100
    assert target.calculate_invoice([item], 0.1) == {
        "subtotal": 300,
        "discount": 30,
        "tax": 27,
        "total": 297,
    }

