from importlib import import_module

cursor = import_module("exercises.api_pagination_deep.01_cursor")


def test_first_page_returns_next_cursor() -> None:
    items = [
        {"id": "u1", "created_at": 1},
        {"id": "u2", "created_at": 2},
        {"id": "u3", "created_at": 3},
    ]

    assert cursor.paginate(items, limit=2) == {
        "items": items[:2],
        "next_cursor": "u2",
    }


def test_after_id_returns_next_page() -> None:
    items = [
        {"id": "u1", "created_at": 1},
        {"id": "u2", "created_at": 2},
        {"id": "u3", "created_at": 3},
    ]

    assert cursor.paginate(items, limit=2, after_id="u2") == {
        "items": [items[2]],
        "next_cursor": None,
    }


def test_unknown_cursor_starts_from_beginning_and_limit_is_capped() -> None:
    items = [{"id": f"u{index}", "created_at": index} for index in range(120)]

    page = cursor.paginate(items, limit=1000, after_id="missing")

    assert len(page["items"]) == 100
    assert page["next_cursor"] == "u99"
