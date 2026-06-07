from importlib import import_module

target = import_module("exercises.settings_secrets.01_settings")


def test_missing_keys() -> None:
    assert target.missing_keys({"APP_ENV": "dev", "TOKEN": ""}, ["APP_ENV", "TOKEN", "DB"]) == [
        "TOKEN",
        "DB",
    ]


def test_mask_secret() -> None:
    assert target.mask_secret(None) == ""
    assert target.mask_secret("abc") == "***"
    assert target.mask_secret("12345678") == "1234...5678"


def test_public_settings() -> None:
    assert target.public_settings({"APP_ENV": "dev", "TOKEN": "secret"}, {"TOKEN"}) == {
        "APP_ENV": "dev",
    }
