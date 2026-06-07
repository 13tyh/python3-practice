"""外部API呼び出しのretry判断を作る練習。"""

RETRYABLE_STATUS_CODES = {408, 429, 500, 502, 503, 504}


def should_retry(status_code: int, attempt: int, max_attempts: int) -> bool:
    """retry可能なstatusで、attemptが上限未満ならTrue。"""
    # TODO
    raise NotImplementedError


def backoff_seconds(attempt: int, base: float = 0.5, cap: float = 8.0) -> float:
    """exponential backoffをcap付きで返す。attemptは1始まり。"""
    # TODO
    raise NotImplementedError


def classify_status(status_code: int) -> str:
    """status codeをsuccess/client_error/retryable_error/server_errorへ分類する。"""
    # TODO
    raise NotImplementedError
