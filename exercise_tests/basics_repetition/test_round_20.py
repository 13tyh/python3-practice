from exercises.basics_repetition.round_20 import Counter, counter_label, increment, reset


def test_round_20() -> None:
    counter = Counter()
    increment(counter)
    increment(counter, 4)
    assert counter.value == 5
    assert counter_label(counter) == "count=5"
    reset(counter)
    assert counter.value == 0
