from importlib import import_module

ops = import_module("exercises.docker_ops.01_health_env")


def test_missing_required_env() -> None:
    assert ops.missing_required_env({"APP_ENV": "dev", "MONGO_URI": "mongodb://mongo"}) == []
    assert ops.missing_required_env({"APP_ENV": "", "OTHER": "x"}) == ["APP_ENV", "MONGO_URI"]


def test_health_status_distinguishes_ok_degraded_and_down() -> None:
    assert ops.health_status(db_ok=True, ai_ok=True) == {"status": "ok"}
    assert ops.health_status(db_ok=True, ai_ok=False) == {"status": "degraded", "reason": "ai"}
    assert ops.health_status(db_ok=False, ai_ok=True) == {"status": "down", "reason": "db"}
