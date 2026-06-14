from importlib import import_module

target = import_module("exercises.data_contracts.01_contracts")


def test_missing_required_fields() -> None:
    assert target.missing_required_fields({"id": "1", "name": "Aki"}, {"id", "email"}) == [
        "email",
    ]


def test_is_compatible() -> None:
    assert target.is_compatible(2, 2) is True
    assert target.is_compatible(3, 2) is False


def test_contract_violations() -> None:
    rows = [{"id": "1", "email": "a@example.com"}, {"id": "2"}, {"email": "b@example.com"}]

    assert target.contract_violations(rows, {"id", "email"}) == [1, 2]
