from importlib import import_module

target = import_module("exercises.n_plus_one_performance.02_bulk_processing")


def test_bulk_processing() -> None:
    assert target.unique_ids(["u1", "u2", "u1"]) == ["u1", "u2"]
    assert target.chunked(["a", "b", "c"], 2) == [["a", "b"], ["c"]]
    assert target.build_in_query("user_id", ["u1", "u2"]) == {"user_id": {"$in": ["u1", "u2"]}}
    rows = [{"id": "u1", "name": "Aki"}, {"id": "u2", "name": "Ren"}]
    assert target.avoid_full_scan_lookup(rows, "id") == {"u1": rows[0], "u2": rows[1]}
