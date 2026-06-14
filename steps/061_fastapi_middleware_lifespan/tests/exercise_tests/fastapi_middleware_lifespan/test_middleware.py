from importlib import import_module

target = import_module("exercises.fastapi_middleware_lifespan.01_middleware")


def test_build_request_log() -> None:
    assert target.build_request_log("r1", "/health", 200, 12) == {
        "request_id": "r1",
        "path": "/health",
        "status_code": 200,
        "latency_ms": 12,
    }


def test_should_enable_cors() -> None:
    assert target.should_enable_cors("https://app.example.com", ["https://app.example.com"])
    assert not target.should_enable_cors("https://evil.example.com", ["https://app.example.com"])


def test_lifespan_event_order() -> None:
    assert target.lifespan_event_order(["mongo", "ai"]) == [
        "connect:mongo",
        "connect:ai",
        "disconnect:ai",
        "disconnect:mongo",
    ]
