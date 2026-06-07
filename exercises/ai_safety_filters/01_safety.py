"""AI safety filterの練習。"""

UNSAFE_KEYWORDS = ("delete database", "steal token", "認証情報を盗む")


def mask_email(text: str) -> str:
    """emailらしき文字列をmaskする。"""
    # TODO
    raise NotImplementedError


def unsafe_reasons(text: str) -> list[str]:
    """危険な意図のkeywordを返す。"""
    # TODO
    raise NotImplementedError


def safety_decision(text: str) -> dict[str, object]:
    """allowとreasonsを含むdictを返す。"""
    # TODO
    raise NotImplementedError
