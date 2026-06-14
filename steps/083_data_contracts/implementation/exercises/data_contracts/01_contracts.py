"""data contractの練習。"""


def missing_required_fields(row: dict[str, object], required: set[str]) -> list[str]:
    """不足している必須fieldを返す。"""
    # TODO
    raise NotImplementedError


def is_compatible(producer_version: int, consumer_supported_version: int) -> bool:
    """producer versionがconsumer対応範囲内ならTrue。"""
    # TODO
    raise NotImplementedError


def contract_violations(rows: list[dict[str, object]], required: set[str]) -> list[int]:
    """contract違反のrow indexを返す。"""
    # TODO
    raise NotImplementedError
