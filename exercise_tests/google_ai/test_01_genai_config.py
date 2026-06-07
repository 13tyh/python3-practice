from importlib import import_module
from types import SimpleNamespace

target = import_module("exercises.google_ai.01_genai_config")


def test_load_settings(monkeypatch) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", "abc")
    monkeypatch.setenv("GOOGLE_GENAI_USE_VERTEXAI", "true")
    monkeypatch.setenv("GOOGLE_CLOUD_PROJECT", "demo")
    settings = target.load_settings()
    assert settings.api_key == "abc"
    assert settings.use_vertexai
    assert settings.project == "demo"


def test_choose_auth_mode() -> None:
    assert target.choose_auth_mode(target.GenAISettings("m", None, True, "p", "global")) == "vertex"
    assert target.choose_auth_mode(target.GenAISettings("m", "k", False, None, "global")) == "api_key"
    assert target.choose_auth_mode(target.GenAISettings("m", None, False, None, "global")) == "missing"


def test_build_prompt() -> None:
    prompt = target.build_prompt("レビュー", "print('x')")
    assert "レビュー" in prompt
    assert "print('x')" in prompt


def test_extract_text() -> None:
    assert target.extract_text(SimpleNamespace(text="hello")) == "hello"
    assert target.extract_text(SimpleNamespace(text=None)) == ""


def test_mask_secret() -> None:
    assert target.mask_secret(None) == ""
    assert target.mask_secret("abc") == "***"
    assert target.mask_secret("123456789") == "1234...6789"

