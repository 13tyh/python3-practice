"""例外処理の練習。"""


def safe_divide(a: int, b: int) -> float | None:
    """0除算ならNone。"""
    # TODO
    raise NotImplementedError


def parse_int(text: str) -> int:
    """整数に変換できなければValueErrorをそのまま出す。"""
    # TODO
    raise NotImplementedError


def require_positive(number: int) -> int:
    """0以下ならValueError。"""
    # TODO
    raise NotImplementedError


def get_required(data: dict[str, str], key: str) -> str:
    """keyがなければKeyErrorをそのまま出す。"""
    # TODO
    raise NotImplementedError
