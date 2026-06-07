from pathlib import Path

from exercises.basics_repetition.round_18 import copy_text, count_words_in_file, write_if_missing


def test_round_18(tmp_path: Path) -> None:
    path = tmp_path / "memo.txt"
    assert write_if_missing(path, "hello world")
    assert not write_if_missing(path, "ignored")
    assert count_words_in_file(path) == 2
    dst = tmp_path / "copy.txt"
    copy_text(path, dst)
    assert dst.read_text(encoding="utf-8") == "hello world"
