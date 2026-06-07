from importlib import import_module

target = import_module("exercises.network_api.01_http_basics")


def test_build_url() -> None:
    assert target.build_url("https://api.example.com/", "/users", {"q": "Aki"}) == (
        "https://api.example.com/users?q=Aki"
    )


def test_build_auth_headers() -> None:
    assert target.build_auth_headers("secret") == {"Authorization": "Bearer secret"}


def test_is_success() -> None:
    assert target.is_success(200)
    assert target.is_success(204)
    assert not target.is_success(404)


def test_extract_items() -> None:
    result = target.ApiResult(200, {"items": [{"id": 1}]})
    assert target.extract_items(result) == [{"id": 1}]
    assert target.extract_items(target.ApiResult(200, {})) == []


def test_safe_error_message() -> None:
    assert target.safe_error_message(404, "not found") == "HTTP 404: not found"

