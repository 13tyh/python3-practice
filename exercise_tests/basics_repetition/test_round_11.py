from exercises.basics_repetition.round_11 import repeat_text, running_total, take_until_negative


def test_round_11() -> None:
    assert list(repeat_text("x", 3)) == ["x", "x", "x"]
    assert running_total([1, 2, 3]) == [1, 3, 6]
    assert take_until_negative([1, 2, -1, 3]) == [1, 2]
