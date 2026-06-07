from importlib import import_module

target = import_module("exercises.rag_deep.04_prompting")


def test_rag_prompting() -> None:
    prompt = target.build_rag_prompt("What is FastAPI?", "FastAPI is Python framework.")
    assert "What is FastAPI?" in prompt
    assert "FastAPI is Python framework." in prompt
    assert target.refusal_message() == "参照情報からは回答できません。"
    assert target.answer_from_context("q", "") == "参照情報からは回答できません。"

