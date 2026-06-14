from importlib import import_module

target = import_module("exercises.ai_observability.01_traces")


def test_latency_bucket() -> None:
    assert target.latency_bucket(300) == "fast"
    assert target.latency_bucket(1500) == "normal"
    assert target.latency_bucket(5000) == "slow"


def test_trace_event() -> None:
    assert target.trace_event("r1", "gemini", "v2", 300) == {
        "request_id": "r1",
        "model_name": "gemini",
        "prompt_version": "v2",
        "latency_bucket": "fast",
    }


def test_usage_context() -> None:
    assert target.usage_context(10, 5, 0.001) == {
        "input_tokens": "10",
        "output_tokens": "5",
        "total_tokens": "15",
        "cost_usd": "0.001000",
    }
