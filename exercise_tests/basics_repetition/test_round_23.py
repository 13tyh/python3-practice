from exercises.basics_repetition.round_23 import has_next_page, page_count, paginate_items


def test_round_23() -> None:
    assert paginate_items(["a", "b", "c"], page=1, per_page=2) == ["a", "b"]
    assert paginate_items(["a", "b", "c"], page=2, per_page=2) == ["c"]
    assert page_count(5, 2) == 3
    assert has_next_page(5, 2, 2)
    assert not has_next_page(4, 2, 2)

