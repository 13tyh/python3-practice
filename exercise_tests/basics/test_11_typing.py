from importlib import import_module

target = import_module("exercises.basics.11_typing")

products = [
    {"id": "p1", "name": "Pen", "price": 120},
    {"id": "p2", "name": "Book", "price": 1200},
]


def test_product_label() -> None:
    assert target.product_label(products[0]) == "p1: Pen (120円)"


def test_expensive_products() -> None:
    assert target.expensive_products(products, 1000) == [products[1]]


def test_index_by_id() -> None:
    assert target.index_by_id(products)["p2"]["name"] == "Book"

