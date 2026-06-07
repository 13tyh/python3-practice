from importlib import import_module
import logging

target = import_module("exercises.logging_python.02_error_logging")


def test_run_with_error_log_success() -> None:
    logger = logging.getLogger("test.success")
    assert target.run_with_error_log(logger, "task", lambda: "ok") == "ok"


def test_run_with_error_log_error(caplog) -> None:
    logger = logging.getLogger("test.error")

    def fail() -> str:
        raise RuntimeError("boom")

    with caplog.at_level(logging.ERROR, logger="test.error"):
        assert target.run_with_error_log(logger, "task", fail) is None
    assert "action failed: task" in caplog.text


def test_should_log_debug() -> None:
    assert target.should_log_debug("local")
    assert target.should_log_debug("dev")
    assert target.should_log_debug("test")
    assert not target.should_log_debug("production")


def test_safe_log_message() -> None:
    assert target.safe_log_message("hello\nworld") == "hello world"

