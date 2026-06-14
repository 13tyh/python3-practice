from importlib import import_module

target = import_module("exercises.basics.31_stdlib")


def test_stdlib_tasks() -> None:
    assert target.count_words(["a", "b", "a"])["a"] == 2
    assert target.group_by_first_char(["apple", "api", "book"]) == {
        "a": ["apple", "api"],
        "b": ["book"],
    }
    assert target.flatten_with_chain([[1, 2], [3]]) == [1, 2, 3]
    assert target.most_common_word(["a", "b", "a"]) == "a"
    assert target.most_common_word([]) is None
