from exercises.basics_repetition.round_49 import filter_scores, index_by_id, invert, name_lengths


def test_round_49() -> None:
    assert name_lengths(["Aki", "Ren"]) == {"Aki": 3, "Ren": 3}
    items = [{"id": "u1", "name": "Aki"}, {"id": "u2", "name": "Ren"}]
    assert index_by_id(items) == {"u1": items[0], "u2": items[1]}
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}
    assert filter_scores({"Aki": 90, "Ren": 70}, 80) == {"Aki": 90}
