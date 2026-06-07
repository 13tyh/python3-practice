from importlib import import_module

typing_practice = import_module("exercises.static_typing.01_type_narrowing")


def test_parse_age_accepts_int_and_numeric_string() -> None:
    assert typing_practice.parse_age(20) == 20
    assert typing_practice.parse_age("31") == 31


def test_parse_age_rejects_none_negative_and_text() -> None:
    assert typing_practice.parse_age(None) is None
    assert typing_practice.parse_age("-1") is None
    assert typing_practice.parse_age("old") is None


def test_normalize_user() -> None:
    assert typing_practice.normalize_user({"name": "Aki", "age": "22"}) == {
        "name": "Aki",
        "age": 22,
        "active": True,
    }


def test_normalize_user_rejects_invalid_input() -> None:
    assert typing_practice.normalize_user({"name": "", "age": 22}) is None
    assert typing_practice.normalize_user({"name": "Aki", "age": None}) is None
