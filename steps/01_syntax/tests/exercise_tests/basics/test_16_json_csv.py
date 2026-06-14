from importlib import import_module
from pathlib import Path

target = import_module("exercises.basics.16_json_csv")


def test_json_tasks() -> None:
    text = target.dumps_pretty({"name": "Aki"})
    assert '"name": "Aki"' in text
    assert target.loads_dict('{"score": 90}') == {"score": 90}


def test_csv_tasks(tmp_path: Path) -> None:
    path = tmp_path / "users.csv"
    target.write_csv_rows(path, [{"name": "Aki"}, {"name": "Ren"}])
    assert target.read_csv_names(path) == ["Aki", "Ren"]
