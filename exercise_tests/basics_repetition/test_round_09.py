from pathlib import Path

from exercises.basics_repetition.round_09 import load_user, safe_load_user, save_user, user_summary


def test_round_09(tmp_path: Path) -> None:
    path = tmp_path / "user.json"
    save_user(path, {"id": "u1", "name": "Aki"})
    user = load_user(path)
    assert user == {"id": "u1", "name": "Aki"}
    assert user_summary(user) == "u1:Aki"
    assert safe_load_user(tmp_path / "missing.json") == {}

