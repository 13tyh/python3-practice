from importlib import import_module

etl = import_module("exercises.etl_pipeline.01_streaming_csv")


def test_iter_valid_rows_filters_invalid_rows() -> None:
    rows = [
        {"topic": "python", "minutes": "30"},
        {"topic": "", "minutes": "10"},
        {"topic": "db", "minutes": "bad"},
        {"topic": "ai", "minutes": "0"},
    ]

    assert list(etl.iter_valid_rows(rows)) == [{"topic": "python", "minutes": "30"}]


def test_summarize_minutes_groups_by_topic() -> None:
    rows = [
        {"topic": "python", "minutes": "30"},
        {"topic": "python", "minutes": "20"},
        {"topic": "db", "minutes": "15"},
        {"topic": "db", "minutes": "-1"},
    ]

    assert etl.summarize_minutes(rows) == {"python": 50, "db": 15}
