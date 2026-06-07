"""小さな実務風タスク。"""


def build_query(params: dict[str, str | None]) -> dict[str, str]:
    """Noneと空文字を除いた検索条件を返す。"""
    # TODO
    raise NotImplementedError


def validate_user_input(data: dict[str, str]) -> list[str]:
    """name/emailが空ならエラーメッセージを返す。"""
    # TODO
    raise NotImplementedError


def calculate_cart(items: list[dict[str, int]]) -> dict[str, int]:
    """subtotal, tax, total を返す。税率10%。"""
    # TODO
    raise NotImplementedError
