from importlib import import_module

target = import_module("exercises.property_thinking.01_invariants")


def test_normalize_tags() -> None:
    assert target.normalize_tags([" Python ", "api", "PYTHON", "", "Db"]) == [
        "api",
        "db",
        "python",
    ]


def test_is_idempotent_normalization() -> None:
    assert target.is_idempotent_normalization([" Python ", "PYTHON", "api"]) is True
