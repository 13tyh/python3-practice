from datetime import date, datetime
from importlib import import_module

target = import_module("exercises.basics.15_datetime")


def test_datetime_tasks() -> None:
    assert target.parse_date("2026-06-07") == date(2026, 6, 7)
    assert target.format_date(date(2026, 6, 7)) == "2026/06/07"
    assert target.days_between(date(2026, 6, 1), date(2026, 6, 7)) == 6
    assert target.add_days(date(2026, 6, 1), 3) == date(2026, 6, 4)
    assert target.parse_iso_datetime("2026-06-07T10:20:30") == datetime(2026, 6, 7, 10, 20, 30)

