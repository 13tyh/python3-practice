from importlib import import_module

target = import_module("exercises.ai_ab_drift.01_ab_drift")


def test_choose_variant_is_stable() -> None:
    assert target.choose_variant("user-1", 0.5) == target.choose_variant("user-1", 0.5)
    assert target.choose_variant("user-1", 0.0) == "A"
    assert target.choose_variant("user-1", 1.0) == "B"


def test_conversion_rate() -> None:
    events = [
        {"variant": "B", "converted": True},
        {"variant": "B", "converted": False},
        {"variant": "A", "converted": True},
    ]

    assert target.conversion_rate(events, "B") == 0.5


def test_drifted_metrics() -> None:
    assert target.drifted_metrics({"accuracy": 0.9}, {"accuracy": 0.7}, 0.1) == ["accuracy"]
