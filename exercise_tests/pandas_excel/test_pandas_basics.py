from importlib import import_module
from pathlib import Path

target = import_module("exercises.pandas_excel.01_pandas_basics")


def test_pandas_basics(tmp_path: Path) -> None:
    csv_path = tmp_path / "sales.csv"
    csv_path.write_text("category,amount\nbook,100\nbook,200\npen,50\n", encoding="utf-8")
    df = target.load_csv(csv_path)
    assert list(df.columns) == ["category", "amount"]

    result = target.total_by_category(df)
    assert result.to_dict("records") == [
        {"category": "book", "amount": 300},
        {"category": "pen", "amount": 50},
    ]

    xlsx_path = tmp_path / "report.xlsx"
    target.export_excel(xlsx_path, {"summary": result})
    assert xlsx_path.exists()
