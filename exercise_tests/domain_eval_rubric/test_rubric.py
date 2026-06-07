from importlib import import_module

target = import_module("exercises.domain_eval_rubric.01_rubric")


def test_weighted_score() -> None:
    scores = {"accuracy": 1.0, "grounding": 1.0, "policy": 0.5, "tone": 0.0}

    assert target.weighted_score(scores) == 0.8


def test_passed() -> None:
    assert target.passed({"accuracy": 1, "grounding": 1, "policy": 1, "tone": 1}) is True


def test_weak_dimensions() -> None:
    assert target.weak_dimensions({"accuracy": 0.6, "grounding": 0.9}) == ["accuracy"]
