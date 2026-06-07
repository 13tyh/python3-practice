"""dataclass の追加練習。"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Address:
    city: str
    postal_code: str


@dataclass
class Customer:
    id: str
    name: str
    address: Address
    tags: list[str] = field(default_factory=list)


def customer_label(customer: Customer) -> str:
    # TODO
    raise NotImplementedError


def add_tag(customer: Customer, tag: str) -> None:
    # TODO
    raise NotImplementedError


def move_customer(customer: Customer, address: Address) -> Customer:
    # TODO
    raise NotImplementedError

