from exercises.basics_repetition.round_32 import User, admin_users, rename_user, user_map


def test_round_32() -> None:
    users = [User("u1", "Aki", "admin"), User("u2", "Ren", "member")]
    assert admin_users(users) == [users[0]]
    assert user_map(users) == {"u1": users[0], "u2": users[1]}
    assert rename_user(users[0], "Mio") == User("u1", "Mio", "admin")
