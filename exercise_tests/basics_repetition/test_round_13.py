import pytest

from exercises.basics_repetition.round_13 import env_bool, env_list, require_positive_env


def test_round_13(monkeypatch) -> None:
    monkeypatch.setenv("FEATURE", "true")
    monkeypatch.setenv("NAMES", "Aki,Ren,Mio")
    monkeypatch.setenv("LIMIT", "10")
    assert env_bool("FEATURE")
    assert env_list("NAMES") == ["Aki", "Ren", "Mio"]
    assert require_positive_env("LIMIT") == 10
    monkeypatch.setenv("LIMIT", "0")
    with pytest.raises(ValueError):
        require_positive_env("LIMIT")
