from importlib import import_module

target = import_module("exercises.basic_import_modules.01_import_rules")


def test_build_public_name() -> None:
    assert target.build_public_name("app.service", "create_user") == "app.service.create_user"


def test_is_private_name() -> None:
    assert target.is_private_name("_helper") is True
    assert target.is_private_name("service") is False


def test_detect_circular_risk() -> None:
    imports = {
        "router": ["service"],
        "service": ["model", "router"],
        "model": [],
    }

    assert target.detect_circular_risk(imports) == [("router", "service")]
