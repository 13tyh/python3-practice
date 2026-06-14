"""AI observability traceの練習。"""


def latency_bucket(duration_ms: int) -> str:
    """durationをfast/normal/slowへ分類する。"""
    # TODO
    raise NotImplementedError


def trace_event(
    request_id: str,
    model_name: str,
    prompt_version: str,
    duration_ms: int,
) -> dict[str, str]:
    """AI呼び出しのtrace eventを作る。"""
    # TODO
    raise NotImplementedError


def usage_context(input_tokens: int, output_tokens: int, cost_usd: float) -> dict[str, str]:
    """token/costをログ用dictへ変換する。"""
    # TODO
    raise NotImplementedError
