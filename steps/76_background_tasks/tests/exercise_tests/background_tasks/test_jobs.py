from importlib import import_module

target = import_module("exercises.background_tasks.01_jobs")


def test_create_job_rejects_duplicate_key() -> None:
    existing = [target.Job("j1", "pending", "k1")]

    assert target.create_job(existing, "j2", "k1") is None
    assert target.create_job(existing, "j2", "k2") == target.Job("j2", "pending", "k2")


def test_next_pending_job_and_complete() -> None:
    jobs = [target.Job("j1", "running", "k1"), target.Job("j2", "pending", "k2")]

    assert target.next_pending_job(jobs) == jobs[1]
    assert target.complete_job(jobs[1], succeeded=True).status == "succeeded"
    assert target.complete_job(jobs[1], succeeded=False).status == "failed"
