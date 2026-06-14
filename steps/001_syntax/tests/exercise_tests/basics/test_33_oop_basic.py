from importlib import import_module

import pytest

target = import_module("exercises.basics.33_oop_basic")


def test_oop_basic_tasks() -> None:
    account = target.BankAccount("Aki", 100)
    account.deposit(50)
    assert account.get_balance() == 150
    account.withdraw(30)
    assert account.get_balance() == 120
    with pytest.raises(ValueError):
        account.withdraw(999)

    savings = target.SavingsAccount("Ren", 1000)
    savings.add_interest(0.1)
    assert savings.get_balance() == 1100
