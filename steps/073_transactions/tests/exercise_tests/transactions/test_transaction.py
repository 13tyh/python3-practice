from importlib import import_module

target = import_module("exercises.transactions.01_transaction")


def test_transaction() -> None:
    tx = target.FakeTransaction()
    assert target.run_in_transaction(tx, should_fail=False) == "committed"
    assert tx.committed

    tx = target.FakeTransaction()
    assert target.run_in_transaction(tx, should_fail=True) == "rolled_back"
    assert tx.rolled_back
    assert target.should_use_transaction(2, True)
    assert not target.should_use_transaction(1, False)
