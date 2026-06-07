from importlib import import_module
from pathlib import Path

target = import_module("exercises.basics.08_files")


def test_file_tasks(tmp_path: Path) -> None:
    path = tmp_path / "memo.txt"
    target.write_lines(path, ["a", "b"])
    assert target.read_lines(path) == ["a", "b"]
    target.append_log(path, "c")
    assert target.read_lines(path) == ["a", "b", "c"]
    assert target.count_lines(path) == 3

