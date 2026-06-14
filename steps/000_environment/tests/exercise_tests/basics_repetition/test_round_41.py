from exercises.basics_repetition.round_41 import (
    count_long_words,
    double_numbers,
    join_with_comma,
    total,
)


def test_round_41() -> None:
    assert double_numbers([1, 2, 3]) == [2, 4, 6]
    assert total([1, 2, 3]) == 6
    assert count_long_words(["a", "python", "go"], 3) == 1
    assert join_with_comma(["a", "b", "c"]) == "a,b,c"
