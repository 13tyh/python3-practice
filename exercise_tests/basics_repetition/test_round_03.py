from pathlib import Path

from exercises.basics_repetition.round_03 import (
    append_line,
    first_word,
    mask_token,
    read_non_empty_lines,
    sort_scores,
)


def test_round_03(tmp_path: Path) -> None:
    assert first_word(" hello python ") == "hello"
    assert first_word("   ") is None
    assert sort_scores({"Aki": 90, "Ren": 70}) == [("Aki", 90), ("Ren", 70)]
    path = tmp_path / "memo.txt"
    append_line(path, "a")
    append_line(path, "")
    append_line(path, "b")
    assert read_non_empty_lines(path) == ["a", "b"]
    assert mask_token("1234567890") == "1234...7890"

