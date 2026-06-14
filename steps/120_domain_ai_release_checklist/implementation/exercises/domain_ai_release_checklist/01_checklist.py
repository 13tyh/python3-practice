"""特化型AI release checklistの練習。"""

REQUIRED_CHECKS = {"eval_passed", "logging_ready", "safety_reviewed", "fallback_ready"}


def incomplete_checks(checks: dict[str, bool]) -> list[str]:
    """未完了の必須checkを返す。"""
    # TODO
    raise NotImplementedError


def can_release(checks: dict[str, bool]) -> bool:
    """必須checkがすべてTrueならrelease可能。"""
    # TODO
    raise NotImplementedError


def monitoring_metrics() -> list[str]:
    """release後に見るmetric名を返す。"""
    # TODO
    raise NotImplementedError
