from importlib import import_module

target = import_module("exercises.basic_context_manager.01_context_manager")


def test_timer_log_records_exit() -> None:
    events: list[str] = []

    with target.TimerLog(events, "job"):
        events.append("running")

    assert events == ["start:job", "running", "end:job"]


def test_temporary_setting_restores_value() -> None:
    settings = {"mode": "prod"}

    with target.temporary_setting(settings, "mode", "test"):
        assert settings["mode"] == "test"

    assert settings["mode"] == "prod"


def test_write_lines(tmp_path) -> None:
    path = tmp_path / "out.txt"

    target.write_lines(str(path), ["a", "b"])

    assert path.read_text(encoding="utf-8") == "a\nb\n"
