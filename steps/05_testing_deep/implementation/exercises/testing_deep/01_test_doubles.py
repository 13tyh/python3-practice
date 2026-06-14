"""test double / fake client の練習。"""

from typing import Protocol


class PaymentClient(Protocol):
    def charge(self, user_id: str, amount: int) -> bool:
        """Charge user."""


class FakePaymentClient:
    def __init__(self, should_succeed: bool = True) -> None:
        self.should_succeed = should_succeed
        self.calls: list[tuple[str, int]] = []

    def charge(self, user_id: str, amount: int) -> bool:
        self.calls.append((user_id, amount))
        return self.should_succeed


def checkout(user_id: str, amount: int, client: PaymentClient) -> str:
    # TODO
    raise NotImplementedError


def build_param_cases() -> list[tuple[int, str]]:
    # TODO
    raise NotImplementedError
