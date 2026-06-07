from exercises.basics_repetition.round_06 import (
    count_roles,
    has_duplicate,
    normalize_tags,
    pick_fields,
    total_amount,
)


def test_round_06() -> None:
    assert normalize_tags([" Python ", "python", "API"]) == ["python", "api"]
    assert count_roles([{"role": "admin"}, {"role": "member"}, {"role": "member"}]) == {
        "admin": 1,
        "member": 2,
    }
    assert total_amount([{"amount": "100"}, {"amount": "250"}]) == 350
    assert has_duplicate(["a", "b", "a"])
    assert not has_duplicate(["a", "b"])
    assert pick_fields({"id": "1", "name": "Aki"}, ["name"]) == {"name": "Aki"}

