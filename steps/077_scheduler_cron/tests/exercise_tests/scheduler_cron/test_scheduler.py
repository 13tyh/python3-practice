from datetime import date
from importlib import import_module

target = import_module("exercises.scheduler_cron.01_scheduler")


def test_due_jobs() -> None:
    jobs = [
        {"id": "a", "enabled": True, "next_run": date(2026, 6, 1)},
        {"id": "b", "enabled": False, "next_run": date(2026, 6, 1)},
        {"id": "c", "enabled": True, "next_run": date(2026, 6, 9)},
    ]

    assert target.due_jobs(jobs, date(2026, 6, 7)) == ["a"]


def test_next_daily_run() -> None:
    assert target.next_daily_run(date(2026, 6, 7), 1) == date(2026, 6, 8)
    assert target.next_daily_run(date(2026, 6, 7), 7) == date(2026, 6, 14)
