from exercises.basics_repetition.round_45 import active_users, count_active, find_user_name, user_names


def test_round_45() -> None:
    users = [
        {"id": "u1", "name": "Aki", "active": True},
        {"id": "u2", "name": "Ren", "active": False},
    ]
    assert active_users(users) == [users[0]]
    assert user_names(users) == ["Aki", "Ren"]
    assert count_active(users) == 1
    assert find_user_name(users, "u1") == "Aki"
    assert find_user_name(users, "missing") is None

