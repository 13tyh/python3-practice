from importlib import import_module

target = import_module("exercises.core_design_thinking.02_boundaries")


def test_boundaries() -> None:
    assert target.age_group(0) == "child"
    assert target.age_group(17) == "child"
    assert target.age_group(18) == "adult"
    assert target.age_group(64) == "adult"
    assert target.age_group(65) == "senior"
    assert target.clamp_page(0) == 1
    assert target.clamp_page(3) == 3
    assert target.safe_ratio(1, 0) == 0.0
    assert target.safe_ratio(1, 4) == 0.25

