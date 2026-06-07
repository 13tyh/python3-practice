"""import / module設計の基礎練習。"""

__all__ = ["PUBLIC_SETTING", "build_public_name", "detect_circular_risk"]

PUBLIC_SETTING = "enabled"
_PRIVATE_PREFIX = "_"


def build_public_name(module_name: str, symbol: str) -> str:
    """module.symbolの表示名を返す。"""
    # TODO
    raise NotImplementedError


def is_private_name(name: str) -> bool:
    """先頭underscoreならprivate扱い。"""
    # TODO
    raise NotImplementedError


def detect_circular_risk(imports: dict[str, list[str]]) -> list[tuple[str, str]]:
    """A->BかつB->Aのimport関係を検出する。"""
    # TODO
    raise NotImplementedError
