from exercises.basics_repetition.round_24 import average_grade, grade, normalize_score


def test_round_24() -> None:
    assert normalize_score(80, 100) == 0.8
    assert normalize_score(1, 0) == 0.0
    assert grade(90) == "A"
    assert grade(75) == "B"
    assert grade(50) == "C"
    assert average_grade([90, 80]) == "A"
    assert average_grade([]) == "C"
