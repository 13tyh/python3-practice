from exercises.basics_repetition.round_52 import all_positive, any_long_word, joined_upper, sum_squares


def test_round_52() -> None:
    assert sum_squares([1, 2, 3]) == 14
    assert any_long_word(["a", "python"], 5)
    assert not any_long_word(["a", "go"], 5)
    assert all_positive([1, 2, 3])
    assert not all_positive([1, 0, 3])
    assert joined_upper(["a", "b"]) == "A,B"

