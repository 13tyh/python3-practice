from importlib import import_module

target = import_module("exercises.domain_ai_release_checklist.01_checklist")


def test_incomplete_checks() -> None:
    assert target.incomplete_checks({"eval_passed": True, "logging_ready": False}) == [
        "fallback_ready",
        "logging_ready",
        "safety_reviewed",
    ]


def test_can_release() -> None:
    checks = {
        "eval_passed": True,
        "logging_ready": True,
        "safety_reviewed": True,
        "fallback_ready": True,
    }

    assert target.can_release(checks) is True


def test_monitoring_metrics() -> None:
    assert target.monitoring_metrics() == [
        "latency_ms",
        "error_rate",
        "fallback_rate",
        "bad_answer_rate",
    ]
