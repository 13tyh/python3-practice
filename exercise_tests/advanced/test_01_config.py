from importlib import import_module

target = import_module("exercises.advanced.01_config")


def test_load_config(monkeypatch) -> None:
    monkeypatch.setenv("APP_ENV", "production")
    monkeypatch.setenv("DEBUG", "false")
    monkeypatch.setenv("MONGO_URI", "mongodb://localhost:27017")
    config = target.load_config()
    assert config.env == "production"
    assert not config.debug
    assert target.is_production(config)

