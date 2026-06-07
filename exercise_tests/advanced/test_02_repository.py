from importlib import import_module

import pytest

target = import_module("exercises.advanced.02_repository")


def test_repository() -> None:
    repo = target.InMemoryTaskRepository()
    task = target.Task("1", "learn python")
    repo.add(task)
    assert repo.find_by_id("1") == task
    assert repo.list_all() == [task]
    assert repo.mark_done("1") == target.Task("1", "learn python", True)
    with pytest.raises(KeyError):
        repo.mark_done("missing")

