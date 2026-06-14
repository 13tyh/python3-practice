from exercises.basics_repetition.round_54 import (
    active_user_ids,
    role_labels,
    score_rows,
    user_names,
)


def test_round_54() -> None:
    users = [
        {"id": "u1", "name": "Aki", "role": "admin", "active": True},
        {"id": "u2", "name": "Ren", "role": "member", "active": False},
    ]
    assert user_names(users) == ["Aki", "Ren"]
    assert active_user_ids(users) == ["u1"]
    assert role_labels(users) == ["Aki(admin)", "Ren(member)"]
    assert score_rows({"Aki": 90}) == [{"name": "Aki", "score": 90}]
