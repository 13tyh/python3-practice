import pytest

from exercises.basics_repetition.round_08 import (
    contains_keyword,
    extract_domain,
    is_postal_code,
    replace_tabs,
)


def test_round_08() -> None:
    assert contains_keyword("Hello Python", "python")
    assert extract_domain("aki@example.com") == "example.com"
    with pytest.raises(ValueError):
        extract_domain("invalid")
    assert replace_tabs("a\tb\tc") == "a b c"
    assert is_postal_code("123-4567")
    assert not is_postal_code("1234567")

