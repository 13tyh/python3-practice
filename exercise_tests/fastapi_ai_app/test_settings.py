from exercises.fastapi_ai_app.settings import AISettings, load_ai_settings, validate_ai_settings


def test_load_ai_settings(monkeypatch) -> None:
    monkeypatch.setenv("AI_PROVIDER", "gemini")
    monkeypatch.setenv("AI_MODEL", "gemini-2.5-flash")
    monkeypatch.setenv("AI_TIMEOUT_SECONDS", "20")
    assert load_ai_settings() == AISettings("gemini", "gemini-2.5-flash", 20)


def test_validate_ai_settings() -> None:
    assert validate_ai_settings(AISettings("fake", "test-model", 10)) == []
    assert validate_ai_settings(AISettings("", "", 0)) == [
        "provider is required",
        "model is required",
        "timeout_seconds must be positive",
    ]
