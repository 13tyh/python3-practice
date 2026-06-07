from importlib import import_module

target = import_module("exercises.basics.03_loops")


def test_sum_numbers() -> None:
    assert target.sum_numbers([1, 2, 3]) == 6


def test_count_even() -> None:
    assert target.count_even([1, 2, 4, 5]) == 2


def test_collect_short_words() -> None:
    assert target.collect_short_words(["a", "python", "go"], 2) == ["a", "go"]


def test_fizzbuzz() -> None:
    assert target.fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert target.fizzbuzz(15)[-1] == "FizzBuzz"

