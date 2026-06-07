from importlib import import_module
from pathlib import Path

target = import_module("exercises.core_design_thinking.07_pure_side_effect")


def test_pure_side_effect(tmp_path: Path) -> None:
    rows = [{"name": "Aki", "score": "90"}, {"name": "Ren", "score": "80"}]
    assert target.build_report_text(rows) == "Aki: 90\nRen: 80\n"
    path = tmp_path / "report.txt"
    target.create_report(path, rows)
    assert path.read_text(encoding="utf-8") == "Aki: 90\nRen: 80\n"

