from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderItem:
    name: str
    unit_price: int
    quantity: int


def calculate_order_total(items: list[OrderItem], discount_rate: float = 0) -> int:
    subtotal = sum(item.unit_price * item.quantity for item in items)
    discounted = subtotal * (1 - discount_rate)
    return round(discounted)


def can_free_ship(total: int, prefecture: str) -> bool:
    threshold = 5000
    if prefecture in {"北海道", "沖縄"}:
        threshold = 8000
    return total >= threshold
