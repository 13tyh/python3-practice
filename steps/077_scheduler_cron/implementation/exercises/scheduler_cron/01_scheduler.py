"""schedulerとcron的処理の練習。"""

from datetime import date


def due_jobs(jobs: list[dict[str, object]], today: date) -> list[str]:
    """enabledでnext_runがtoday以前のjob idを返す。"""
    # TODO
    raise NotImplementedError


def next_daily_run(today: date, interval_days: int) -> date:
    """daily batchの次回実行日を返す。"""
    # TODO
    raise NotImplementedError
