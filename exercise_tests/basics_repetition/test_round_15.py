from exercises.basics_repetition.round_15 import (
    build_order_response,
    order_status_label,
    order_total,
    validate_order,
)


def test_round_15() -> None:
    order = {"id": "o1", "items": [{"price": 100, "quantity": 2}], "status": "paid"}
    assert validate_order(order) == []
    assert validate_order({"items": []}) == ["id is required", "items are required"]
    assert order_total(order) == 200
    assert order_status_label("paid") == "支払い済み"
    assert order_status_label("unknown") == "不明"
    assert build_order_response(order) == {
        "id": "o1",
        "total": 200,
        "status_label": "支払い済み",
    }

