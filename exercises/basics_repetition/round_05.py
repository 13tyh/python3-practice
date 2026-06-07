"""基礎反復 round 05."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    name: str
    price: int
    stock: int


def product_label(product: Product) -> str:
    # TODO
    raise NotImplementedError


def in_stock(products: list[Product]) -> list[Product]:
    # TODO
    raise NotImplementedError


def total_stock_value(products: list[Product]) -> int:
    # TODO
    raise NotImplementedError


def most_expensive(products: list[Product]) -> Product | None:
    # TODO
    raise NotImplementedError


def discount(product: Product, rate: float) -> Product:
    # TODO
    raise NotImplementedError

