from exercises.basics_repetition.round_16 import (
    max_or_none,
    parse_csv_line,
    remove_none,
    strip_or_none,
)


def test_round_16() -> None:
    assert strip_or_none("  Aki ") == "Aki"
    assert strip_or_none("   ") is None
    assert strip_or_none(None) is None
    assert parse_csv_line("a, b, c") == ["a", "b", "c"]
    assert max_or_none([1, 3, 2]) == 3
    assert max_or_none([]) is None
    assert remove_none(["a", None, "b"]) == ["a", "b"]
