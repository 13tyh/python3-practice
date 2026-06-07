"""API互換性と破壊的変更の応用練習。"""


def removed_fields(old_fields: list[str], new_fields: list[str]) -> list[str]:
    """削除されたfieldを返す。"""
    # TODO
    raise NotImplementedError


def is_breaking_required_change(old_required: list[str], new_required: list[str]) -> bool:
    """新しいrequiredが増えたら破壊的変更。"""
    # TODO
    raise NotImplementedError


def deprecation_headers(version: str, sunset: str) -> dict[str, str]:
    """非推奨API用headerを返す。"""
    # TODO
    raise NotImplementedError
