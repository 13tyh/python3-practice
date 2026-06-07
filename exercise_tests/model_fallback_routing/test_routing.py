from importlib import import_module

target = import_module("exercises.model_fallback_routing.01_routing")


def test_route_deployment() -> None:
    assert target.route_deployment("chat") == "fast"
    assert target.route_deployment("code_review") == "strong"
    assert target.route_deployment("unknown") == "fast"


def test_next_fallback() -> None:
    assert target.next_fallback("fast", ["fast", "strong"]) == "strong"
    assert target.next_fallback("strong", ["fast", "strong"]) is None


def test_should_fallback() -> None:
    assert target.should_fallback("timeout") is True
    assert target.should_fallback("validation_error") is False
