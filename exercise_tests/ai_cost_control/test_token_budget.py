from importlib import import_module

cost = import_module("exercises.ai_cost_control.01_token_budget")


def test_estimate_tokens_uses_minimum_one_token() -> None:
    assert cost.estimate_tokens("") == 1
    assert cost.estimate_tokens("abcd") == 1
    assert cost.estimate_tokens("abcde") == 2


def test_fits_budget_checks_model_limit() -> None:
    assert cost.fits_budget("hello", 100, "gemini-2.5-flash") is True
    assert cost.fits_budget("x" * 40000, 1000, "gemini-2.5-flash") is False


def test_choose_model_uses_deployment_mapping() -> None:
    mapping = {
        "fast": "gemini-2.5-flash",
        "large": "gemini-2.5-pro",
    }

    assert cost.choose_model("short prompt", mapping) == "gemini-2.5-flash"
    assert cost.choose_model("x" * 40000, mapping) == "gemini-2.5-pro"
