from exercises.basics_repetition.round_42 import countdown, repeat_until_length, sum_until


def test_round_42() -> None:
    assert countdown(3) == [3, 2, 1]
    assert countdown(0) == []
    assert repeat_until_length("ab", 5) == "ababa"
    assert sum_until(4) == 10
