from pathlib import Path

from exercises.file_db_export.csv_export import export_documents_to_csv, read_csv, write_csv
from exercises.file_db_export.transform import document_to_row, documents_to_rows, normalize_value


def test_transform() -> None:
    assert normalize_value(None) == ""
    assert normalize_value(123) == "123"
    assert document_to_row({"name": "Aki", "score": 90}, ["name", "score", "missing"]) == {
        "name": "Aki",
        "score": "90",
        "missing": "",
    }
    assert documents_to_rows([{"name": "Aki"}], ["name"]) == [{"name": "Aki"}]


def test_csv_export(tmp_path: Path) -> None:
    path = tmp_path / "users.csv"
    rows = [{"name": "Aki", "score": "90"}]
    write_csv(path, rows, ["name", "score"])
    assert read_csv(path) == rows

    exported = tmp_path / "export.csv"
    export_documents_to_csv(exported, [{"name": "Ren", "score": 80}], ["name", "score"])
    assert read_csv(exported) == [{"name": "Ren", "score": "80"}]

