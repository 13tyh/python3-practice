from exercises.basics_repetition.round_46 import lengths, squares, strip_all, upper_words


def test_round_46() -> None:
    assert squares([1, 2, 3]) == [1, 4, 9]
    assert upper_words(["a", "Py"]) == ["A", "PY"]
    assert lengths(["a", "python"]) == [1, 6]
    assert strip_all([" a ", " b"]) == ["a", "b"]

