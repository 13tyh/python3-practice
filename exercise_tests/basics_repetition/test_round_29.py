from exercises.basics_repetition.round_29 import count_log_levels, error_messages, parse_log_line


def test_round_29() -> None:
    assert parse_log_line("INFO:login:ok") == {"level": "INFO", "action": "login", "message": "ok"}
    lines = ["INFO:login:ok", "ERROR:review:failed", "ERROR:chat:timeout"]
    assert count_log_levels(lines) == {"INFO": 1, "ERROR": 2}
    assert error_messages(lines) == ["failed", "timeout"]

