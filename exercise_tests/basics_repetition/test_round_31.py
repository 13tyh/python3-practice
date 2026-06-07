from pathlib import Path

from exercises.basics_repetition.round_31 import next_available_path, read_or_default, write_lines_numbered


def test_round_31(tmp_path: Path) -> None:
    path = tmp_path / "report.txt"
    assert next_available_path(path) == path
    path.write_text("exists", encoding="utf-8")
    assert next_available_path(path) == tmp_path / "report_1.txt"
    assert read_or_default(tmp_path / "missing.txt", "none") == "none"
    out = tmp_path / "lines.txt"
    write_lines_numbered(out, ["a", "b"])
    assert out.read_text(encoding="utf-8") == "1. a\n2. b\n"

