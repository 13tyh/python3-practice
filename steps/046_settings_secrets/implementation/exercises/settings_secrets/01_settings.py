"""settingsとsecret管理の練習。"""


def missing_keys(env: dict[str, str], required: list[str]) -> list[str]:
    """存在しないか空文字のkeyを返す。"""
    # TODO
    raise NotImplementedError


def mask_secret(value: str | None) -> str:
    """secretをログ用にmaskする。"""
    # TODO
    raise NotImplementedError


def public_settings(settings: dict[str, str], secret_keys: set[str]) -> dict[str, str]:
    """secret keyを除いたsettingsを返す。"""
    # TODO
    raise NotImplementedError
