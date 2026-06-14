from importlib import import_module

target = import_module("exercises.dependency_injection.01_di")


def test_dependency_injection() -> None:
    repo = target.create_repository({"u1": "Aki"})
    assert target.greet_user("u1", repo) == "Hello, Aki"
    assert target.greet_user("missing", repo) == "Hello, Guest"
