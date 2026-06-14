"""datetime timezone の練習。"""

from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=9))


def now_utc() -> datetime:
    # TODO
    raise NotImplementedError


def to_jst(value: datetime) -> datetime:
    # TODO
    raise NotImplementedError


def parse_iso8601(text: str) -> datetime:
    # TODO
    raise NotImplementedError


def is_aware(value: datetime) -> bool:
    # TODO
    raise NotImplementedError
