import logging
from importlib import import_module

target = import_module("exercises.logging_python.01_logger_basics")


def test_get_logger() -> None:
    logger = target.get_logger("app.service")
    assert logger.name == "app.service"


def test_parse_log_level() -> None:
    assert target.parse_log_level("debug") == logging.DEBUG
    assert target.parse_log_level("INFO") == logging.INFO
    assert target.parse_log_level("unknown") == logging.INFO


def test_mask_value() -> None:
    assert target.mask_value(None) == ""
    assert target.mask_value("abc") == "***"
    assert target.mask_value("1234567890") == "1234...7890"


def test_build_log_context() -> None:
    assert target.build_log_context("u1", "login", "ok") == {
        "user_id": "u1",
        "action": "login",
        "status": "ok",
    }


def test_log_success(caplog) -> None:
    logger = logging.getLogger("test.log_success")
    with caplog.at_level(logging.INFO, logger="test.log_success"):
        target.log_success(logger, "login", "u1")
    assert "action=login user_id=u1 status=ok" in caplog.text
