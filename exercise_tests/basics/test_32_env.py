from importlib import import_module

import pytest

target = import_module("exercises.basics.32_env")


def test_env_tasks(monkeypatch) -> None:
    monkeypatch.setenv("APP_NAME", "python-master")
    monkeypatch.setenv("PORT", "8000")
    assert target.get_env("APP_NAME", "default") == "python-master"
    assert target.get_env("MISSING", "default") == "default"
    assert target.require_env("APP_NAME") == "python-master"
    with pytest.raises(RuntimeError):
        target.require_env("MISSING")
    assert target.get_int_env("PORT", 3000) == 8000
    assert target.get_int_env("MISSING_PORT", 3000) == 3000
