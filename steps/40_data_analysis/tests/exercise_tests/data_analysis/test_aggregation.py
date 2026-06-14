from importlib import import_module

target = import_module("exercises.data_analysis.02_aggregation")


def test_aggregation() -> None:
    rows = [
        {"category": "book", "amount": 100},
        {"category": "book", "amount": 200},
        {"category": "pen", "amount": 50},
    ]
    assert target.sum_by_key(rows, "category", "amount") == {"book": 300, "pen": 50}
    assert target.average_by_key(rows, "category", "amount") == {"book": 150.0, "pen": 50.0}
    assert target.top_n(rows, "amount", 2) == rows[:2]
