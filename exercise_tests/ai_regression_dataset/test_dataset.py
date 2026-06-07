from importlib import import_module

target = import_module("exercises.ai_regression_dataset.01_dataset")


def test_score_case() -> None:
    assert target.score_case({"expected": "ok", "actual": "ok"}) is True
    assert target.score_case({"expected": "ok", "actual": "ng"}) is False


def test_failure_cases() -> None:
    cases = [{"expected": "ok", "actual": "ok"}, {"expected": "ok", "actual": "ng"}]

    assert target.failure_cases(cases) == [cases[1]]


def test_accuracy_by_model() -> None:
    cases = [
        {"model": "fast", "expected": "ok", "actual": "ok"},
        {"model": "fast", "expected": "ok", "actual": "ng"},
        {"model": "strong", "expected": "ok", "actual": "ok"},
    ]

    assert target.accuracy_by_model(cases) == {"fast": 0.5, "strong": 1.0}
