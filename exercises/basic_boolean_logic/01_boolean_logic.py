"""bool条件を読みやすくする練習。"""


def is_blank(value: str | None) -> bool:
    """Noneまたは空白だけの文字列ならTrue。"""
    # TODO
    raise NotImplementedError


def can_access(is_active: bool, has_role: bool, is_locked: bool) -> bool:
    """activeでroleがあり、lockedでない時だけTrue。"""
    # TODO
    raise NotImplementedError


def should_send_email(email: str | None, unsubscribed: bool) -> bool:
    """emailがあり、unsubscribeされていなければTrue。"""
    # TODO
    raise NotImplementedError
