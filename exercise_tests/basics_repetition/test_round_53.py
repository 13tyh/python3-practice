from exercises.basics_repetition.round_53 import indexed_map, number_items, pair_sums, zip_to_dict


def test_round_53() -> None:
    assert number_items(["a", "b"]) == ["1: a", "2: b"]
    assert zip_to_dict(["a", "b"], [1, 2]) == {"a": 1, "b": 2}
    assert indexed_map(["a", "b"]) == {0: "a", 1: "b"}
    assert pair_sums([1, 2], [10, 20]) == [11, 22]
