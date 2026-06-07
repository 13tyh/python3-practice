from importlib import import_module

target = import_module("exercises.git_workflow.01_status_parser")


def test_parse_short_status() -> None:
    assert target.parse_short_status([" M app.py", "A  new.py", "?? memo.md"]) == {
        "modified": ["app.py"],
        "added": ["new.py"],
        "untracked": ["memo.md"],
    }


def test_branch_summary() -> None:
    assert target.branch_summary("## master...origin/master [ahead 1, behind 2]") == {
        "branch": "master",
        "upstream": "origin/master",
        "ahead": 1,
        "behind": 2,
    }
