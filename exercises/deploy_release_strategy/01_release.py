"""blue/green / canary / rollbackの応用練習。"""


def canary_percentage(stage: str) -> int:
    """stageからcanary割合を返す。"""
    # TODO
    raise NotImplementedError


def should_rollback(error_rate: float, max_error_rate: float, health: str) -> bool:
    """error率超過またはunhealthyならrollback。"""
    # TODO
    raise NotImplementedError


def active_color(current: str, target: str) -> str:
    """blue/green切替後のactive colorを返す。"""
    # TODO
    raise NotImplementedError
