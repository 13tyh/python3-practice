from importlib import import_module

retry = import_module("exercises.resilience.01_retry_policy")


def test_should_retry_only_retryable_status_before_limit() -> None:
    assert retry.should_retry(503, attempt=1, max_attempts=3) is True
    assert retry.should_retry(400, attempt=1, max_attempts=3) is False
    assert retry.should_retry(503, attempt=3, max_attempts=3) is False


def test_backoff_seconds_is_exponential_and_capped() -> None:
    assert retry.backoff_seconds(1) == 0.5
    assert retry.backoff_seconds(3) == 2.0
    assert retry.backoff_seconds(10) == 8.0


def test_classify_status() -> None:
    assert retry.classify_status(200) == "success"
    assert retry.classify_status(404) == "client_error"
    assert retry.classify_status(429) == "retryable_error"
    assert retry.classify_status(501) == "server_error"
