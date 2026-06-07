from exercises.basics_repetition.round_50 import duplicate_values, even_set, first_letters, unique_lower


def test_round_50() -> None:
    assert unique_lower(["A", "a", "B"]) == {"a", "b"}
    assert first_letters(["apple", "book"]) == {"a", "b"}
    assert even_set([1, 2, 2, 3, 4]) == {2, 4}
    assert duplicate_values(["a", "b", "a", "c", "b"]) == {"a", "b"}

