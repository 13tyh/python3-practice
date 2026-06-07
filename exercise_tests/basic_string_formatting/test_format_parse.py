from importlib import import_module

target = import_module("exercises.basic_string_formatting.01_format_parse")


def test_display_user() -> None:
    assert target.display_user("Aki", 20) == "Aki (20)"


def test_parse_csv_line() -> None:
    assert target.parse_csv_line(" Aki, 20, Tokyo ") == ["Aki", "20", "Tokyo"]


def test_normalize_spaces() -> None:
    assert target.normalize_spaces("  Python   is  fun ") == "Python is fun"
