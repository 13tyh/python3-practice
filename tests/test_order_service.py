from mastery.order_service import OrderItem, calculate_order_total, can_free_ship


def test_calculate_order_total() -> None:
    items = [OrderItem("book", 1200, 2), OrderItem("pen", 100, 3)]
    assert calculate_order_total(items) == 2700
    assert calculate_order_total(items, discount_rate=0.1) == 2430


def test_can_free_ship() -> None:
    assert can_free_ship(5000, "東京")
    assert not can_free_ship(5000, "北海道")
    assert can_free_ship(8000, "沖縄")
