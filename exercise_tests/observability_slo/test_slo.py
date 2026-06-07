from importlib import import_module

target = import_module("exercises.observability_slo.01_slo")


def test_error_rate() -> None:
    assert target.error_rate(100, 5) == 0.05
    assert target.error_rate(0, 5) == 0.0


def test_burn_rate() -> None:
    assert target.burn_rate(0.05, 0.01) == 5


def test_should_alert() -> None:
    assert target.should_alert(0.2, 100, 0.1, 500)
    assert target.should_alert(0.01, 800, 0.1, 500)
    assert not target.should_alert(0.01, 100, 0.1, 500)
