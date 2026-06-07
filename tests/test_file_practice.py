from pathlib import Path

from mastery.file_practice import load_json, read_text, sum_csv_amounts, write_json


def test_file_operations(tmp_path: Path) -> None:
    text_path = tmp_path / "memo.txt"
    text_path.write_text("hello", encoding="utf-8")
    assert read_text(text_path) == "hello"

    json_path = tmp_path / "data.json"
    write_json(json_path, {"name": "Aki", "score": 90})
    assert load_json(json_path)["score"] == 90

    csv_path = tmp_path / "sales.csv"
    csv_path.write_text("name,amount\nbook,1200\npen,300\n", encoding="utf-8")
    assert sum_csv_amounts(csv_path) == 1500
