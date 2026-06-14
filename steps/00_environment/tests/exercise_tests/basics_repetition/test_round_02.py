import pytest

from exercises.basics_repetition.round_02 import (
    count_by_value,
    merge_unique,
    normalize_email,
    require_key,
    safe_int,
)


def test_round_02() -> None:
    assert normalize_email("  AKI@EXAMPLE.COM ") == "aki@example.com"
    assert safe_int("10") == 10
    assert safe_int("x", default=5) == 5
    assert count_by_value(["a", "b", "a"]) == {"a": 2, "b": 1}
    assert merge_unique(["a", "b"], ["b", "c"]) == ["a", "b", "c"]
    assert require_key({"name": "Aki"}, "name") == "Aki"
    with pytest.raises(KeyError):
        require_key({}, "name")
