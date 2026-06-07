from datetime import UTC, datetime
from importlib import import_module

target = import_module("exercises.datetime_timezone.01_timezone")


def test_timezone() -> None:
    value = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
    assert target.to_jst(value).hour == 9
    assert target.parse_iso8601("2026-01-01T00:00:00+00:00").tzinfo is not None
    assert target.is_aware(value)
    assert not target.is_aware(datetime(2026, 1, 1))
    assert target.now_utc().tzinfo == UTC

