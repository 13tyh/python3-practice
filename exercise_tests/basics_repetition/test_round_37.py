from exercises.basics_repetition.round_37 import bigger, can_buy, is_positive, is_zero, sign_label


def test_round_37() -> None:
    assert is_zero(0)
    assert not is_zero(1)
    assert is_positive(1)
    assert not is_positive(0)
    assert bigger(3, 5) == 5
    assert sign_label(10) == "positive"
    assert sign_label(0) == "zero"
    assert sign_label(-1) == "negative"
    assert can_buy(100, 100)
    assert not can_buy(101, 100)

