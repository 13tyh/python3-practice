from exercises.basics_repetition.round_28 import inventory_value, low_stock_names, restock


def test_round_28() -> None:
    items = [
        {"name": "Pen", "price": 100, "stock": 3},
        {"name": "Book", "price": 1200, "stock": 0},
    ]
    assert inventory_value(items) == 300
    assert low_stock_names(items, 1) == ["Book"]
    assert restock(items[1], 5) == {"name": "Book", "price": 1200, "stock": 5}
    assert items[1]["stock"] == 0

