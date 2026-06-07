from importlib import import_module

target = import_module("exercises.observability.01_observability")


def test_observability() -> None:
    ctx = target.RequestContext("req-1", "u1", "/reviews")
    assert target.build_log_event(ctx, "create_review", "ok") == {
        "request_id": "req-1",
        "user_id": "u1",
        "path": "/reviews",
        "action": "create_review",
        "status": "ok",
    }
    assert target.metric_name("ai_review", "create", "count") == "ai_review.create.count"
    assert target.trace_parent("child", "parent") == {"span": "child", "parent_span": "parent"}

