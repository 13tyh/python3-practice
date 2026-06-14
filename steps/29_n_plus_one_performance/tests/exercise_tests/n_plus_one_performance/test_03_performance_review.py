from importlib import import_module

target = import_module("exercises.n_plus_one_performance.03_performance_review")


def test_performance_review() -> None:
    assert target.has_db_call_in_loop(["for user in users:", "    repo.find_orders(user.id)"])
    assert target.has_db_call_in_loop(["for user in users:", "    db.orders.find(...)"])
    assert not target.has_db_call_in_loop(["orders = repo.find_orders_by_user_ids(ids)"])
    assert target.estimate_n_plus_one_queries(10) == 11
    assert target.is_better_query_count(11, 2)
    assert not target.is_better_query_count(2, 2)
