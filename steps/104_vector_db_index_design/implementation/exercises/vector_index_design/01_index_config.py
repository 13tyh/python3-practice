"""vector index設計の練習。"""

ALLOWED_METRICS = {"cosine", "dotproduct", "euclidean"}


def normalize_metric(metric: str) -> str:
    """metricを小文字化し、許可されない値ならValueError。"""
    # TODO
    raise NotImplementedError


def validate_dimension(vector: list[float], expected_dimension: int) -> bool:
    """vector dimensionが一致すればTrue。"""
    # TODO
    raise NotImplementedError


def build_index_config(dimension: int, metric: str, filter_fields: list[str]) -> dict[str, object]:
    """vector index設定をdictで返す。"""
    # TODO
    raise NotImplementedError
