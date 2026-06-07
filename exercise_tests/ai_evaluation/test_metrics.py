from importlib import import_module

target = import_module("exercises.ai_evaluation.01_metrics")


def test_ai_metrics() -> None:
    rows = [
        {"expected": "ok", "actual": "ok", "reason": "", "prompt": "v1"},
        {"expected": "ok", "actual": "ng", "reason": "format", "prompt": "v1"},
        {"expected": "ng", "actual": "ng", "reason": "", "prompt": "v2"},
    ]
    assert target.accuracy(rows) == 2 / 3
    assert target.count_fail_reasons(rows) == {"format": 1}
    assert target.compare_prompt_accuracy(rows) == {"v1": 0.5, "v2": 1.0}
