from exercises.basics_repetition.round_44 import receipt_line, subtotal, tax, total_price


def test_round_44() -> None:
    assert subtotal(100, 3) == 300
    assert tax(1000) == 100
    assert total_price(100, 3) == 330
    assert receipt_line("Pen", 100, 3) == "Pen: 100 x 3 = 330"
