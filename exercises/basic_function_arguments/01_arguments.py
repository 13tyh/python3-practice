"""関数引数の基礎練習。"""


def greet(name: str, greeting: str = "Hello") -> str:
    """default引数を使って挨拶を返す。"""
    # TODO
    raise NotImplementedError


def make_page(*, page: int = 1, size: int = 20) -> dict[str, int]:
    """keyword-only引数でpage設定を作る。"""
    # TODO
    raise NotImplementedError


def pick_option(options: dict[str, object], key: str, default: object) -> object:
    """kwargs的なdictから安全に値を読む。"""
    # TODO
    raise NotImplementedError
