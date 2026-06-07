from importlib import import_module

target = import_module("exercises.basics.23_regex")


def test_regex_tasks() -> None:
    assert target.contains_number("abc123")
    assert not target.contains_number("abc")
    assert target.extract_numbers("a12 b3") == ["12", "3"]
    assert target.is_simple_phone_number("090-1234-5678")
    assert not target.is_simple_phone_number("09012345678")
    assert target.replace_spaces("hello   python\tworld") == "hello python world"
