from pathlib import Path

from exercises.basics_repetition.round_14 import ensure_parent, list_files_by_suffix, make_report_path


def test_round_14(tmp_path: Path) -> None:
    assert make_report_path(tmp_path, "sales report") == tmp_path / "sales_report.md"
    path = tmp_path / "logs" / "app.log"
    ensure_parent(path)
    assert path.parent.is_dir()
    (tmp_path / "a.py").write_text("", encoding="utf-8")
    (tmp_path / "b.txt").write_text("", encoding="utf-8")
    assert list_files_by_suffix(tmp_path, ".py") == [tmp_path / "a.py"]

