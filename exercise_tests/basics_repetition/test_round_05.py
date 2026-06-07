from exercises.basics_repetition.round_05 import (
    Product,
    discount,
    in_stock,
    most_expensive,
    product_label,
    total_stock_value,
)


def test_round_05() -> None:
    pen = Product("Pen", 100, 3)
    book = Product("Book", 1200, 0)
    assert product_label(pen) == "Pen: 100円 x 3"
    assert in_stock([pen, book]) == [pen]
    assert total_stock_value([pen, book]) == 300
    assert most_expensive([pen, book]) == book
    assert most_expensive([]) is None
    assert discount(book, 0.25) == Product("Book", 900, 0)

