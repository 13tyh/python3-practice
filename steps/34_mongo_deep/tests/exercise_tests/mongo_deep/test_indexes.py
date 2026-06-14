from importlib import import_module

target = import_module("exercises.mongo_deep.01_indexes")


def test_mongo_deep() -> None:
    assert target.single_index("created_at", True) == [("created_at", -1)]
    assert target.compound_index(["user_id", "created_at"]) == [("user_id", 1), ("created_at", 1)]
    assert target.build_upsert_update({"name": "Aki"}) == {"$set": {"name": "Aki"}}
    assert target.explain_uses_index({"queryPlanner": {"winningPlan": {"stage": "IXSCAN"}}})
    assert not target.explain_uses_index({"queryPlanner": {"winningPlan": {"stage": "COLLSCAN"}}})
