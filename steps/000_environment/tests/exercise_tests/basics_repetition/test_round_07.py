from datetime import date

from exercises.basics_repetition.round_07 import (
    days_until,
    format_japanese_date,
    is_weekend_name,
    parse_ymd,
)


def test_round_07() -> None:
    assert parse_ymd("2026-06-07") == date(2026, 6, 7)
    assert days_until(date(2026, 6, 1), date(2026, 6, 7)) == 6
    assert format_japanese_date(date(2026, 6, 7)) == "2026年06月07日"
    assert is_weekend_name("Saturday")
    assert is_weekend_name("日曜日")
    assert not is_weekend_name("Monday")
