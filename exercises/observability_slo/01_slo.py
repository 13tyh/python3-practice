"""OpenTelemetry / SLO / alertの応用練習。"""


def error_rate(total: int, errors: int) -> float:
    """error率を返す。total 0なら0.0。"""
    # TODO
    raise NotImplementedError


def burn_rate(current_error_rate: float, error_budget: float) -> float:
    """現在のerror率がbudgetの何倍か返す。"""
    # TODO
    raise NotImplementedError


def should_alert(
    error_rate_value: float, latency_p95_ms: int, max_error_rate: float, max_latency_ms: int
) -> bool:
    """error率またはlatencyが閾値超えならTrue。"""
    # TODO
    raise NotImplementedError
