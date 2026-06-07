from exercises.basics_repetition.round_47 import (
    adult_ages,
    non_empty_words,
    positive_numbers,
    short_words,
)


def test_round_47() -> None:
    assert positive_numbers([-1, 0, 2]) == [2]
    assert non_empty_words(["a", "", "  ", "b"]) == ["a", "b"]
    assert adult_ages([17, 18, 20]) == [18, 20]
    assert short_words(["a", "python", "go"], 2) == ["a", "go"]
