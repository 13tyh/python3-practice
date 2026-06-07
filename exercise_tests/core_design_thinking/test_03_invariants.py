from importlib import import_module

import pytest

target = import_module("exercises.core_design_thinking.03_invariants")


def test_invariants() -> None:
    target.validate_balance(0)
    with pytest.raises(ValueError):
        target.validate_balance(-1)
    assert target.withdraw(100, 30) == 70
    with pytest.raises(ValueError):
        target.withdraw(100, 200)
    assert target.transfer(100, 50, 30) == (70, 80)

