from exercises.fastapi_ai_app.errors import (
    AIOutputError,
    AIUnavailableError,
    error_to_response,
    is_retryable,
)
from exercises.fastapi_ai_app.usage import (
    TokenUsage,
    estimate_cost_usd,
    total_tokens,
    usage_log_context,
)


def test_errors() -> None:
    assert error_to_response(AIOutputError("bad json")) == {
        "status_code": 422,
        "detail": "bad json",
    }
    assert is_retryable(AIUnavailableError("timeout"))
    assert not is_retryable(AIOutputError("bad output"))


def test_usage() -> None:
    usage = TokenUsage(1000, 500, "gpt-4.1-mini")
    assert total_tokens(usage) == 1500
    assert estimate_cost_usd(usage, 0.01) == 0.015
    assert usage_log_context(usage) == {
        "input_tokens": "1000",
        "output_tokens": "500",
        "total_tokens": "1500",
        "model_name": "gpt-4.1-mini",
    }
