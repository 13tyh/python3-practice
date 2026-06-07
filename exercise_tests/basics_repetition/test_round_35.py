from exercises.basics_repetition.round_35 import clamp_score, pass_fail, summarize_results


def test_round_35() -> None:
    assert clamp_score(-10) == 0
    assert clamp_score(120) == 100
    assert clamp_score(80) == 80
    assert pass_fail(60) == "pass"
    assert pass_fail(59) == "fail"
    assert summarize_results([60, 40, 80]) == {"pass": 2, "fail": 1}
