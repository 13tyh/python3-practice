from pathlib import Path

from exercises.fastapi_ai_app.prompt_loader import (
    default_review_prompt_path,
    load_prompt_template,
    render_prompt,
)


def test_load_prompt_template(tmp_path: Path) -> None:
    path = tmp_path / "prompt.md"
    path.write_text("hello {name}", encoding="utf-8")
    assert load_prompt_template(path) == "hello {name}"


def test_render_prompt() -> None:
    assert render_prompt("hello {name}", {"name": "Aki"}) == "hello Aki"


def test_default_review_prompt_path() -> None:
    assert default_review_prompt_path().name == "review_prompt.md"

