from importlib import import_module

target = import_module("exercises.auth_jwt_rbac.01_auth")


def test_parse_bearer_token() -> None:
    assert target.parse_bearer_token("Bearer abc") == "abc"
    assert target.parse_bearer_token("Basic abc") is None
    assert target.parse_bearer_token(None) is None


def test_has_permission() -> None:
    permissions = {"admin": ["read", "write"], "viewer": ["read"]}

    assert target.has_permission("admin", "write", permissions)
    assert not target.has_permission("viewer", "write", permissions)


def test_build_claims_and_expiration() -> None:
    assert target.build_claims("u1", "admin", 100) == {
        "sub": "u1",
        "role": "admin",
        "exp": 100,
    }
    assert target.is_token_expired(100, 100)
    assert not target.is_token_expired(99, 100)
