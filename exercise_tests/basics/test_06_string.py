from importlib import import_module

target = import_module("exercises.basics.06_string")


def test_normalize_space() -> None:
    assert target.normalize_space("  hello   python  ") == "hello python"


def test_mask_email() -> None:
    assert target.mask_email("taro@example.com") == "t***@example.com"


def test_count_word() -> None:
    assert target.count_word("python java python", "python") == 2


def test_slugify() -> None:
    assert target.slugify("Hello Python World") == "hello-python-world"

