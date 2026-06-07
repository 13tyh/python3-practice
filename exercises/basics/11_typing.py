"""型ヒントの練習。"""

from typing import TypedDict


class Product(TypedDict):
    id: str
    name: str
    price: int


def product_label(product: Product) -> str:
    """例: p01: Pen (120円)."""
    # TODO
    raise NotImplementedError


def expensive_products(products: list[Product], min_price: int) -> list[Product]:
    # TODO
    raise NotImplementedError


def index_by_id(products: list[Product]) -> dict[str, Product]:
    # TODO
    raise NotImplementedError

