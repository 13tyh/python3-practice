from importlib import import_module

target = import_module("exercises.basic_unpacking.01_unpacking")


def test_first_and_rest() -> None:
    assert target.first_and_rest([1, 2, 3]) == (1, [2, 3])
    assert target.first_and_rest([]) == (None, [])


def test_pairs_to_dict() -> None:
    assert target.pairs_to_dict([("name", "Aki"), ("role", "admin")]) == {
        "name": "Aki",
        "role": "admin",
    }


def test_format_point() -> None:
    assert target.format_point((1, 2)) == "x=1, y=2"
