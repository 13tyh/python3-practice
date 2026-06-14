from importlib import import_module

target = import_module("exercises.basic_scope_modules.01_scope")


def test_price_with_tax() -> None:
    assert target.price_with_tax(100) == 110


def test_build_label() -> None:
    assert target.build_label("user", "Aki") == "user:Aki"


def test_public_summary() -> None:
    assert target.public_summary("Aki", 80) == {"name": "Aki", "score": 80, "passed": True}
