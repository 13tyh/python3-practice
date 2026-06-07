from importlib import import_module

target = import_module("exercises.core_design_thinking.01_idempotency")


def test_idempotency() -> None:
    assert target.add_once(["a"], "a") == ["a"]
    assert target.add_once(["a"], "b") == ["a", "b"]
    record = {"id": "1"}
    assert target.mark_processed(record) == {"id": "1", "processed": True}
    assert record == {"id": "1"}
    assert target.idempotency_key("post", "/reviews", "abc") == "POST:/reviews:abc"

