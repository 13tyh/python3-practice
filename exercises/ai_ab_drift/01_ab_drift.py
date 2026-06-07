"""AI A/B test / drift検知の応用練習。"""


def choose_variant(user_id: str, b_ratio: float) -> str:
    """user_idから安定してA/Bを割り当てる。"""
    # TODO
    raise NotImplementedError


def conversion_rate(events: list[dict[str, object]], variant: str) -> float:
    """variantごとのconversion率を返す。"""
    # TODO
    raise NotImplementedError


def drifted_metrics(
    baseline: dict[str, float], current: dict[str, float], threshold: float
) -> list[str]:
    """差分がthresholdを超えたmetric名を返す。"""
    # TODO
    raise NotImplementedError
