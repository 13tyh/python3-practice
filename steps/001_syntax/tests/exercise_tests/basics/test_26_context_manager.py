from importlib import import_module
from pathlib import Path

target = import_module("exercises.basics.26_context_manager")


def test_context_manager_tasks(tmp_path: Path) -> None:
    path = tmp_path / "memo.txt"
    path.write_text("first\nsecond\n", encoding="utf-8")
    assert target.read_first_line(path) == "first"
    assert target.write_and_read(path, "hello") == "hello"

    resource = target.SimpleResource()
    with resource as opened:
        assert opened.opened
    assert not resource.opened
