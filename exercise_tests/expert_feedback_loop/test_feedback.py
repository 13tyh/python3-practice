from importlib import import_module

target = import_module("exercises.expert_feedback_loop.01_feedback")


def test_feedback_counts() -> None:
    feedback = [
        {"reason": "missing_source"},
        {"reason": "wrong_rule"},
        {"reason": "missing_source"},
    ]

    assert target.feedback_counts(feedback) == {"missing_source": 2, "wrong_rule": 1}


def test_top_feedback_reason() -> None:
    assert target.top_feedback_reason([{"reason": "a"}, {"reason": "b"}, {"reason": "a"}]) == "a"
    assert target.top_feedback_reason([]) is None


def test_next_improvement_action() -> None:
    assert target.next_improvement_action("missing_source") == "improve_retrieval"
    assert target.next_improvement_action("wrong_rule") == "update_policy"
