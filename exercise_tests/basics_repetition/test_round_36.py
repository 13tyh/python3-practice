from exercises.basics_repetition.round_36 import add, divide_floor, multiply, remainder, subtract


def test_round_36() -> None:
    assert add(2, 3) == 5
    assert subtract(10, 4) == 6
    assert multiply(3, 4) == 12
    assert divide_floor(7, 2) == 3
    assert remainder(7, 2) == 1
