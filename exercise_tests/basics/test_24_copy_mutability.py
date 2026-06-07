from importlib import import_module

target = import_module("exercises.basics.24_copy_mutability")


def test_copy_mutability_tasks() -> None:
    items = ["a"]
    assert target.append_without_mutating(items, "b") == ["a", "b"]
    assert items == ["a"]

    user = {"name": "Aki", "score": 80}
    updated = target.update_score_without_mutating(user, 90)
    assert updated == {"name": "Aki", "score": 90}
    assert user == {"name": "Aki", "score": 80}

    rows = [{"name": "Aki"}]
    copied = target.shallow_copy_items(rows)
    assert copied == rows
    assert copied is not rows
    assert copied[0] is rows[0]

    nested = [{"tags": ["python"]}]
    deep = target.deep_copy_items(nested)
    assert deep == nested
    assert deep is not nested
    assert deep[0]["tags"] is not nested[0]["tags"]
