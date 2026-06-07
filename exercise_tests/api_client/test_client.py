from importlib import import_module

target = import_module("exercises.api_client.01_client")


def test_api_client() -> None:
    config = target.ApiClientConfig("https://api.example.com/", 10, 3)
    assert target.build_url(config, "/users") == "https://api.example.com/users"
    assert target.should_retry_status(429)
    assert target.should_retry_status(500)
    assert not target.should_retry_status(400)
    assert target.backoff_seconds(3) == 4

