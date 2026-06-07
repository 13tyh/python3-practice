from importlib import import_module

target = import_module("exercises.adrs.01_decision_record")


def test_adr_title() -> None:
    assert target.adr_title(1, "Use FastAPI for AI API") == "0001-use-fastapi-for-ai-api"


def test_decision_summary() -> None:
    body = target.decision_summary("AI APIが必要", "FastAPIを使う", ["型とdocsが強い"])

    assert "## Context" in body
    assert "AI APIが必要" in body
    assert "FastAPIを使う" in body
    assert "型とdocsが強い" in body


def test_format_tradeoffs() -> None:
    assert target.format_tradeoffs(["速い", ""], ["学習コスト"]) == {
        "pros": ["速い"],
        "cons": ["学習コスト"],
    }
