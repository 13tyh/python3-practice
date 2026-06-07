from importlib import import_module

migration = import_module("exercises.schema_evolution.01_migration_plan")


def test_needs_backfill_only_when_field_missing() -> None:
    assert migration.needs_backfill({"name": "Aki"}, "status") is True
    assert migration.needs_backfill({"name": "Aki", "status": None}, "status") is False


def test_build_set_update() -> None:
    assert migration.build_set_update("status", "active") == {"$set": {"status": "active"}}


def test_migration_summary_counts_targets() -> None:
    documents = [
        {"_id": "1", "status": "active"},
        {"_id": "2"},
        {"_id": "3"},
    ]

    assert migration.migration_summary(documents, "status") == {"total": 3, "backfill": 2}
