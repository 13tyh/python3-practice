"""model fallback routingの練習。"""


def route_deployment(task: str) -> str:
    """task種別からdeploymentを選ぶ。"""
    # TODO
    raise NotImplementedError


def next_fallback(current: str, fallback_order: list[str]) -> str | None:
    """currentの次のfallbackを返す。"""
    # TODO
    raise NotImplementedError


def should_fallback(error_type: str) -> bool:
    """timeout/rate_limitだけfallback可能にする。"""
    # TODO
    raise NotImplementedError
