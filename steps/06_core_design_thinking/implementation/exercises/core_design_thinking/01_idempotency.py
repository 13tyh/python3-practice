"""冪等性の練習。"""


def add_once(items: list[str], item: str) -> list[str]:
    """同じ item を何度追加しても1つだけ。"""
    # TODO
    raise NotImplementedError


def mark_processed(record: dict[str, object]) -> dict[str, object]:
    """何度実行しても processed=True。元の dict は変更しない。"""
    # TODO
    raise NotImplementedError


def idempotency_key(method: str, path: str, body_hash: str) -> str:
    # TODO
    raise NotImplementedError
