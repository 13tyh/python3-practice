from importlib import import_module

target = import_module("exercises.refactoring.02_code_smells")


def test_code_smells() -> None:
    assert target.has_long_function(51)
    assert not target.has_long_function(20)
    assert target.has_too_many_args(6)
    assert target.suggest_refactor("long_function") == "extract smaller functions"
    assert target.suggest_refactor("unknown") == "write characterization tests first"
