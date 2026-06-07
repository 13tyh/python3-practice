from importlib import import_module

target = import_module("exercises.feature_flags.01_flags")


def test_rollout_bucket_is_stable() -> None:
    assert target.rollout_bucket("user-1") == target.rollout_bucket("user-1")
    assert 0 <= target.rollout_bucket("user-1") <= 99


def test_is_enabled() -> None:
    assert target.is_enabled({"enabled": False, "rollout_percent": 100}, "user-1") is False
    assert target.is_enabled({"enabled": True, "rollout_percent": 100}, "user-1") is True
    assert target.is_enabled({"enabled": True, "rollout_percent": 0}, "user-1") is False
