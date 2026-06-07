from importlib import import_module

target = import_module("exercises.advanced.04_pagination")


def test_pagination() -> None:
    assert target.paginate(["a", "b", "c"], 1, 2) == ["a", "b"]
    assert target.paginate(["a", "b", "c"], 2, 2) == ["c"]
    assert target.total_pages(5, 2) == 3
    assert target.build_page_info(5, 2, 2) == {
        "page": 2,
        "per_page": 2,
        "total_pages": 3,
        "has_next": True,
        "has_prev": True,
    }

