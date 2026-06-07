from importlib import import_module

target = import_module("exercises.auth.01_auth_basics")


def test_auth_basics() -> None:
    assert target.extract_bearer_token("Bearer abc") == "abc"
    assert target.extract_bearer_token("Basic abc") is None
    assert target.is_valid_api_key("k1", {"k1"})
    assert not target.is_valid_api_key(None, {"k1"})
    assert target.has_permission(["admin"], "admin")
    assert target.mask_token("1234567890") == "1234...7890"

