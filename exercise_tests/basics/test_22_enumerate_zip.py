from importlib import import_module

target = import_module("exercises.basics.22_enumerate_zip")


def test_enumerate_zip_tasks() -> None:
    assert target.number_lines(["a", "b"]) == ["1: a", "2: b"]
    assert target.pair_names_scores(["Aki", "Ren"], [90, 80]) == [
        {"name": "Aki", "score": 90},
        {"name": "Ren", "score": 80},
    ]
    assert target.find_index(["a", "b"], "b") == 1
    assert target.find_index(["a", "b"], "x") is None
    assert target.merge_keys_values(["a", "b"], [1, 2]) == {"a": 1, "b": 2}
