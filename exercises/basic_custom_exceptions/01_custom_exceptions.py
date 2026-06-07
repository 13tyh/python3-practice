"""独自例外の基礎練習。"""


class ValidationError(Exception):
    """入力検証に失敗した時の例外。"""


def validate_age(age: int) -> int:
    """0以上ならageを返し、負数ならValidationError。"""
    # TODO
    raise NotImplementedError


def safe_error_message(error: Exception) -> str:
    """例外を利用者向けの安全なmessageへ変換する。"""
    # TODO
    raise NotImplementedError
