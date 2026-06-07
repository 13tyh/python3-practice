from importlib import import_module

target = import_module("exercises.deploy_release_strategy.01_release")


def test_canary_percentage() -> None:
    assert target.canary_percentage("start") == 5
    assert target.canary_percentage("half") == 50
    assert target.canary_percentage("full") == 100


def test_should_rollback() -> None:
    assert target.should_rollback(0.2, 0.1, "healthy")
    assert target.should_rollback(0.01, 0.1, "unhealthy")
    assert not target.should_rollback(0.01, 0.1, "healthy")


def test_active_color() -> None:
    assert target.active_color("blue", "green") == "green"
