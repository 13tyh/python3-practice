from importlib import import_module

target = import_module("exercises.api_compatibility_design.01_compatibility")


def test_removed_fields() -> None:
    assert target.removed_fields(["id", "name", "email"], ["id", "name"]) == ["email"]


def test_is_breaking_required_change() -> None:
    assert target.is_breaking_required_change(["id"], ["id", "name"])
    assert not target.is_breaking_required_change(["id"], ["id"])


def test_deprecation_headers() -> None:
    assert target.deprecation_headers("v1", "2026-12-31") == {
        "Deprecation": "v1",
        "Sunset": "2026-12-31",
    }
