"""bool / None の練習。"""


def is_blank(text: str | None) -> bool:
    # TODO
    raise NotImplementedError


def default_if_none(value: str | None, default: str) -> str:
    # TODO
    raise NotImplementedError


def to_bool(text: str) -> bool:
    """true/yes/1/on なら True。それ以外は False。大文字小文字は無視。"""
    # TODO
    raise NotImplementedError


def all_present(values: list[str | None]) -> bool:
    """None と空文字がなければ True。"""
    # TODO
    raise NotImplementedError


def any_empty(values: list[str | None]) -> bool:
    """None または空文字が1つでもあれば True。"""
    # TODO
    raise NotImplementedError

