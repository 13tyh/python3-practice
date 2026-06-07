from exercises.basics_repetition.round_22 import highlight_keyword, search_names, startswith_any


def test_round_22() -> None:
    assert search_names(["Aki", "Ren", "Akira"], "aki") == ["Aki", "Akira"]
    assert startswith_any("python", ["py", "js"])
    assert not startswith_any("python", ["go"])
    assert highlight_keyword("hello python", "python") == "hello **python**"

