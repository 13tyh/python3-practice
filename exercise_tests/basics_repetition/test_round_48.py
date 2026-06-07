from exercises.basics_repetition.round_48 import labels, mask_empty, normalize_numbers, pass_fail


def test_round_48() -> None:
    assert labels([-1, 0, 1]) == ["negative", "zero", "positive"]
    assert pass_fail([80, 59, 60]) == ["pass", "fail", "pass"]
    assert mask_empty(["a", "", "b"]) == ["a", "(empty)", "b"]
    assert normalize_numbers([-1, 0, 2]) == [0, 0, 2]

