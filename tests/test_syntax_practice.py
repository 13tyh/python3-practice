import pytest

from mastery.syntax_practice import calculate_total, find_user_email, normalize_name


def test_normalize_name() -> None:
    assert normalize_name("  tanaka taro ") == "Tanaka Taro"


def test_calculate_total() -> None:
    assert calculate_total([100, 200], 0.1) == 330


def test_find_user_email() -> None:
    users = [{"id": "u1", "email": "u1@example.com"}]
    assert find_user_email(users, "u1") == "u1@example.com"
    with pytest.raises(ValueError):
        find_user_email(users, "missing")

