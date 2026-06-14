from importlib import import_module

target = import_module("exercises.basic_regex_practical.01_regex")


def test_is_valid_email() -> None:
    assert target.is_valid_email("a@example.com") is True
    assert target.is_valid_email("bad-example") is False


def test_normalize_phone() -> None:
    assert target.normalize_phone("03-1234-5678") == "0312345678"


def test_extract_hashtags() -> None:
    assert target.extract_hashtags("Hello #Python and #AI") == ["python", "ai"]


def test_mask_zip_code() -> None:
    assert target.mask_zip_code("zip is 123-4567") == "zip is ***-****"
