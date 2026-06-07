from importlib import import_module

target = import_module("exercises.streaming_files_large.01_lines")


def test_iter_effective_lines() -> None:
    lines = ["  alpha\n", "\n", "# comment", " beta "]

    assert list(target.iter_effective_lines(lines)) == ["alpha", "beta"]


def test_count_prefix() -> None:
    assert target.count_prefix(["user:1", "group:1", "user:2", "# user:3"], "user:") == 2
