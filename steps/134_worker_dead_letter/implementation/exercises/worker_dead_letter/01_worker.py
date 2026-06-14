"""worker / dead letter queueの応用練習。"""


def next_attempt_delay(attempt: int, base_seconds: int, max_seconds: int) -> int:
    """指数backoffの待ち秒数を返す。"""
    # TODO
    raise NotImplementedError


def should_dead_letter(attempts: int, max_attempts: int, error_type: str) -> bool:
    """再試行上限またはpermanent errorならdead letterへ送る。"""
    # TODO
    raise NotImplementedError


def job_status(done: bool, error: str | None) -> str:
    """job状態をsucceeded/failed/runningへ分類する。"""
    # TODO
    raise NotImplementedError
