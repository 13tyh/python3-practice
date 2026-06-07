from importlib import import_module

target = import_module("exercises.mongo_deep.02_migration")


def test_migration() -> None:
    docs = [{"name": "Aki"}, {"name": "Ren", "role": "admin"}]
    assert target.add_default_field(docs, "role", "member") == [
        {"name": "Aki", "role": "member"},
        {"name": "Ren", "role": "admin"},
    ]
    assert target.rename_field({"old": 1}, "old", "new") == {"new": 1}
    assert target.migration_update_many_filter("role") == {"role": {"$exists": False}}

