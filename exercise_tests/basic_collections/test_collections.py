from collections import Counter
from importlib import import_module

target = import_module("exercises.basic_collections.01_collections")


def test_count_tags() -> None:
    assert target.count_tags(["ai", "python", "ai"]) == Counter({"ai": 2, "python": 1})


def test_group_names_by_role() -> None:
    users = [
        {"name": "sato", "role": "admin"},
        {"name": "suzuki", "role": "member"},
        {"name": "tanaka", "role": "admin"},
    ]

    assert target.group_names_by_role(users) == {
        "admin": ["sato", "tanaka"],
        "member": ["suzuki"],
    }


def test_recent_items() -> None:
    assert target.recent_items(["a", "b", "c", "d"], 2) == ["c", "d"]
