from exercises.file_db_export.query import build_date_range_query, build_projection, build_sort


def test_build_date_range_query() -> None:
    assert build_date_range_query(None, None) == {}
    assert build_date_range_query("2026-01-01", None) == {"created_at": {"$gte": "2026-01-01"}}
    assert build_date_range_query(None, "2026-01-31") == {"created_at": {"$lte": "2026-01-31"}}
    assert build_date_range_query("2026-01-01", "2026-01-31") == {
        "created_at": {"$gte": "2026-01-01", "$lte": "2026-01-31"}
    }


def test_build_projection() -> None:
    assert build_projection(["name", "score"]) == {"_id": 0, "name": 1, "score": 1}


def test_build_sort() -> None:
    assert build_sort("created_at") == [("created_at", 1)]
    assert build_sort("created_at", descending=True) == [("created_at", -1)]

