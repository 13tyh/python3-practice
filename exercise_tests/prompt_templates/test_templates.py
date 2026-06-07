from importlib import import_module

target = import_module("exercises.prompt_templates.01_templates")


def test_missing_variables() -> None:
    assert target.missing_variables("Hello {name}, {topic}", {"name": "Aki"}) == ["topic"]


def test_render_template() -> None:
    assert target.render_template("Review {code}", {"code": "print(1)"}) == "Review print(1)"


def test_build_messages() -> None:
    assert target.build_messages(
        "You are {role}", "Fix {code}", {"role": "reviewer", "code": "x"}
    ) == [
        {"role": "system", "content": "You are reviewer"},
        {"role": "user", "content": "Fix x"},
    ]
