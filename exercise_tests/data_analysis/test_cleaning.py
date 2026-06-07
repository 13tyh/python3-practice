from importlib import import_module

target = import_module("exercises.data_analysis.01_cleaning")


def test_cleaning() -> None:
    rows = [{"name": "Aki"}, {"name": ""}, {"name": None}]
    assert target.remove_empty_rows(rows) == [{"name": "Aki"}]
    assert target.fill_missing([{"name": None}], "name", "unknown") == [{"name": "unknown"}]
    assert target.deduplicate_by_key([{"id": "1"}, {"id": "1"}, {"id": "2"}], "id") == [
        {"id": "1"},
        {"id": "2"},
    ]
    assert target.to_int("10") == 10
    assert target.to_int(None, default=5) == 5
