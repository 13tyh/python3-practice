from importlib import import_module

target = import_module("exercises.rag_ops_quality.01_rag_ops")


def test_needs_reindex() -> None:
    assert target.needs_reindex("2026-01-02T00:00:00", "2026-01-01T00:00:00")
    assert not target.needs_reindex("2026-01-01T00:00:00", "2026-01-02T00:00:00")


def test_search_click_rate() -> None:
    logs = [{"clicked": True}, {"clicked": False}, {"clicked": True}]

    assert target.search_click_rate(logs) == 2 / 3


def test_is_unanswerable() -> None:
    assert target.is_unanswerable([], 0.7)
    assert target.is_unanswerable([0.2, 0.6], 0.7)
    assert not target.is_unanswerable([0.8], 0.7)
