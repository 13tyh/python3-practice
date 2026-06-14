from importlib import import_module

target = import_module("exercises.basic_set_operations.01_sets")


def test_unique_sorted() -> None:
    assert target.unique_sorted(["b", "a", "b"]) == ["a", "b"]


def test_common_tags() -> None:
    assert target.common_tags({"python", "api"}, {"api", "db"}) == {"api"}


def test_missing_permissions() -> None:
    assert target.missing_permissions({"read", "write"}, {"read"}) == {"write"}
