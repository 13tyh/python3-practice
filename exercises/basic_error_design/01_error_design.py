"""エラー設計の基礎練習。"""


class RetryableError(Exception):
    """再試行してよい失敗。"""


class PermanentError(Exception):
    """入力や権限など再試行しても直らない失敗。"""


def classify_status_code(status_code: int) -> str:
    """HTTP statusからretryable/permanent/successを返す。"""
    # TODO
    raise NotImplementedError


def parse_positive_int(value: str) -> int:
    """正の整数文字列をintへ変換する。失敗時はValueError。"""
    # TODO
    raise NotImplementedError


def should_retry(error: Exception) -> bool:
    """例外種別からretry可否を返す。"""
    # TODO
    raise NotImplementedError
