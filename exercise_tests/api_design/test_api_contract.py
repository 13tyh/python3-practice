from importlib import import_module

target = import_module("exercises.api_design.01_api_contract")


def test_api_contract() -> None:
    assert target.build_pagination(2, 10, 25) == {
        "page": 2,
        "per_page": 10,
        "total": 25,
        "total_pages": 3,
        "has_next": True,
        "has_prev": True,
    }
    assert target.parse_sort("-created_at", {"created_at", "name"}) == ("created_at", "desc")
    assert target.parse_sort("name", {"created_at", "name"}) == ("name", "asc")
    assert target.error_response("not_found", "missing", 404) == {
        "error": {"code": "not_found", "message": "missing"},
        "status_code": 404,
    }
    assert target.idempotency_cache_key("POST", "/reviews", "abc") == "POST:/reviews:abc"
