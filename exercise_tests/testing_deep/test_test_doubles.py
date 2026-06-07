from importlib import import_module

target = import_module("exercises.testing_deep.01_test_doubles")


def test_checkout_with_fake() -> None:
    client = target.FakePaymentClient(True)
    assert target.checkout("u1", 1000, client) == "paid"
    assert client.calls == [("u1", 1000)]

    assert target.checkout("u2", 1000, target.FakePaymentClient(False)) == "failed"
    assert target.build_param_cases() == [(0, "invalid"), (100, "paid")]

