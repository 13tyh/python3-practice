from importlib import import_module

target = import_module("exercises.mongo_aggregation.01_pipeline")


def test_pipeline() -> None:
    assert target.match_status("ok") == {"$match": {"status": "ok"}}
    assert target.group_count_by("action") == {"$group": {"_id": "$action", "count": {"$sum": 1}}}
    assert target.sort_by_count() == {"$sort": {"count": -1}}
    assert target.build_status_count_pipeline("ok", "action") == [
        {"$match": {"status": "ok"}},
        {"$group": {"_id": "$action", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
    ]
