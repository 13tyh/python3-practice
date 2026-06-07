from importlib import import_module

target = import_module("exercises.testing_deep.02_monkeypatch_env")


def test_monkeypatch_env(monkeypatch) -> None:
    monkeypatch.setenv("FEATURE_ENABLED", "true")
    monkeypatch.setenv("API_BASE_URL", "https://api.example.com")
    monkeypatch.setenv("API_KEY", "secret")
    assert target.load_feature_flag()
    assert target.choose_endpoint() == "https://api.example.com"
    assert target.build_headers_from_env() == {"Authorization": "Bearer secret"}

