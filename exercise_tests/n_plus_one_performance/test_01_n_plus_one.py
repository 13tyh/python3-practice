from importlib import import_module

target = import_module("exercises.n_plus_one_performance.01_n_plus_one")


def test_n_plus_one() -> None:
    users = [target.User("u1", "Aki"), target.User("u2", "Ren")]
    orders = [target.Order("o1", "u1", 100), target.Order("o2", "u2", 200)]

    bad_repo = target.FakeRepository(users, orders)
    assert target.list_order_rows_bad(bad_repo) == [
        {"order_id": "o1", "user_name": "Aki", "amount": 100},
        {"order_id": "o2", "user_name": "Ren", "amount": 200},
    ]
    assert bad_repo.query_count == 3

    good_repo = target.FakeRepository(users, orders)
    assert target.list_order_rows_good(good_repo) == [
        {"order_id": "o1", "user_name": "Aki", "amount": 100},
        {"order_id": "o2", "user_name": "Ren", "amount": 200},
    ]
    assert good_repo.query_count == 2

    assert target.user_map(users) == {"u1": users[0], "u2": users[1]}
