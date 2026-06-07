from importlib import import_module
from pathlib import Path

target = import_module("exercises.basic_pathlib_glob.01_pathlib_glob")


def test_has_suffix() -> None:
    assert target.has_suffix(Path("app.py"), ".py") is True
    assert target.has_suffix(Path("README.md"), ".py") is False


def test_file_names() -> None:
    assert target.file_names([Path("a/app.py"), Path("README.md")]) == ["app.py", "README.md"]


def test_filter_by_suffix() -> None:
    assert target.filter_by_suffix([Path("a.py"), Path("b.md")], ".py") == [Path("a.py")]
