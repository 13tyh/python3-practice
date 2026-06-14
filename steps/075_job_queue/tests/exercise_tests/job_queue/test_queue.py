from importlib import import_module

target = import_module("exercises.job_queue.01_queue")


def test_queue() -> None:
    queue = []
    job = target.Job("j1", {"x": "1"})
    target.enqueue(queue, job)
    assert queue == [job]
    target.mark_running(job)
    assert job.status == "running"
    assert job.attempts == 1
    job.status = "failed"
    assert target.should_retry(job, 3)
    job.attempts = 3
    assert not target.should_retry(job, 3)
