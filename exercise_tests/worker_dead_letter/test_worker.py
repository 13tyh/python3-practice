from importlib import import_module

target = import_module("exercises.worker_dead_letter.01_worker")


def test_next_attempt_delay() -> None:
    assert target.next_attempt_delay(1, 2, 60) == 2
    assert target.next_attempt_delay(3, 2, 60) == 8
    assert target.next_attempt_delay(10, 2, 60) == 60


def test_should_dead_letter() -> None:
    assert target.should_dead_letter(3, 3, "temporary")
    assert target.should_dead_letter(1, 3, "permanent")
    assert not target.should_dead_letter(1, 3, "temporary")


def test_job_status() -> None:
    assert target.job_status(True, None) == "succeeded"
    assert target.job_status(False, "boom") == "failed"
    assert target.job_status(False, None) == "running"
