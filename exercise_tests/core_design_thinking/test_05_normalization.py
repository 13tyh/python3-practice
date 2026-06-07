from importlib import import_module

target = import_module("exercises.core_design_thinking.05_normalization")


def test_normalization() -> None:
    assert target.normalize_user_input({"name": " Aki ", "email": None}) == {
        "name": "Aki",
        "email": "",
    }
    assert target.normalize_search_keyword("  Python API ") == "python api"
    assert target.normalize_tags([" Python ", "python", "API"]) == ["python", "api"]
