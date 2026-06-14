"""特化型AI評価rubricの練習。"""

WEIGHTS = {"accuracy": 0.4, "grounding": 0.3, "policy": 0.2, "tone": 0.1}


def weighted_score(scores: dict[str, float]) -> float:
    """rubric scoreを0-1で加重平均する。"""
    # TODO
    raise NotImplementedError


def passed(scores: dict[str, float], threshold: float = 0.8) -> bool:
    """weighted scoreがthreshold以上ならTrue。"""
    # TODO
    raise NotImplementedError


def weak_dimensions(scores: dict[str, float], minimum: float = 0.7) -> list[str]:
    """minimum未満の評価軸を返す。"""
    # TODO
    raise NotImplementedError
