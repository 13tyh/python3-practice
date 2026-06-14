"""OOP の基礎練習。"""


class BankAccount:
    def __init__(self, owner: str, balance: int = 0) -> None:
        # TODO
        raise NotImplementedError

    def deposit(self, amount: int) -> None:
        # TODO
        raise NotImplementedError

    def withdraw(self, amount: int) -> None:
        # TODO
        raise NotImplementedError

    def get_balance(self) -> int:
        # TODO
        raise NotImplementedError


class SavingsAccount(BankAccount):
    def add_interest(self, rate: float) -> None:
        # TODO
        raise NotImplementedError
