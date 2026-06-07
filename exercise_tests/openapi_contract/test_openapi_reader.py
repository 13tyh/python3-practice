from importlib import import_module

target = import_module("exercises.openapi_contract.01_openapi_reader")

SCHEMA = {
    "paths": {
        "/users": {
            "get": {"responses": {"200": {}, "401": {}}},
            "post": {"responses": {"201": {}}},
        },
        "/health": {"get": {"responses": {"200": {}}}},
    }
}


def test_paths_by_method() -> None:
    assert target.paths_by_method(SCHEMA, "get") == ["/health", "/users"]


def test_response_codes() -> None:
    assert target.response_codes(SCHEMA, "/users", "get") == ["200", "401"]


def test_has_operation() -> None:
    assert target.has_operation(SCHEMA, "/users", "post") is True
    assert target.has_operation(SCHEMA, "/users", "delete") is False
