from importlib import import_module
from pathlib import Path

target = import_module("exercises.basics.30_pathlib_deep")


def test_pathlib_deep_tasks(tmp_path: Path) -> None:
    path = tmp_path / "sample.txt"
    assert target.file_name(path) == "sample.txt"
    assert target.file_stem(path) == "sample"
    assert target.change_suffix(path, ".md") == tmp_path / "sample.md"
    target.ensure_directory(tmp_path / "logs")
    assert (tmp_path / "logs").is_dir()
    (tmp_path / "a.py").write_text("", encoding="utf-8")
    (tmp_path / "b.txt").write_text("", encoding="utf-8")
    assert target.list_py_files(tmp_path) == [tmp_path / "a.py"]

