from importlib import import_module

target = import_module("exercises.package_design.01_import_rules")


def test_import_rules() -> None:
    assert target.is_private_name("_helper")
    assert not target.is_private_name("service")
    assert target.public_api_names(["run", "_helper", "create"]) == ["run", "create"]
    assert target.is_allowed_import("router", "service")
    assert target.is_allowed_import("service", "repository")
    assert not target.is_allowed_import("repository", "router")

