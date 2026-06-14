from importlib import import_module

target = import_module("exercises.basic_boolean_logic.01_boolean_logic")


def test_is_blank() -> None:
    assert target.is_blank(None) is True
    assert target.is_blank("  ") is True
    assert target.is_blank("python") is False


def test_can_access() -> None:
    assert target.can_access(True, True, False) is True
    assert target.can_access(True, False, False) is False
    assert target.can_access(True, True, True) is False


def test_should_send_email() -> None:
    assert target.should_send_email("a@example.com", False) is True
    assert target.should_send_email(None, False) is False
    assert target.should_send_email("a@example.com", True) is False
