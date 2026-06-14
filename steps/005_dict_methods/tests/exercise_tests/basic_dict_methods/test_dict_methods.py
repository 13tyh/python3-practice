from importlib import import_module

target = import_module("exercises.basic_dict_methods.01_dict_methods")


def test_get_role() -> None:
    assert target.get_role({"role": "admin"}) == "admin"
    assert target.get_role({}) == "guest"


def test_increment_count_does_not_mutate_original() -> None:
    counts = {"python": 1}

    assert target.increment_count(counts, "python") == {"python": 2}
    assert target.increment_count(counts, "db") == {"python": 1, "db": 1}
    assert counts == {"python": 1}


def test_merge_profile() -> None:
    assert target.merge_profile({"name": "Aki"}, {"role": "admin"}) == {
        "name": "Aki",
        "role": "admin",
    }
