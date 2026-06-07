from importlib import import_module

target = import_module("exercises.basics.17_algorithms")


def test_algorithm_tasks() -> None:
    assert target.linear_search(["a", "b"], "b") == 1
    assert target.linear_search(["a", "b"], "x") == -1
    assert target.remove_duplicates(["a", "b", "a"]) == ["a", "b"]
    assert target.count_chars("aba") == {"a": 2, "b": 1}
    assert target.is_palindrome("level")
    assert not target.is_palindrome("python")

