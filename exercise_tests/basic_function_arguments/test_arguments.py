from importlib import import_module

target = import_module("exercises.basic_function_arguments.01_arguments")


def test_greet() -> None:
    assert target.greet("Aki") == "Hello, Aki"
    assert target.greet("Aki", "Hi") == "Hi, Aki"


def test_make_page() -> None:
    assert target.make_page() == {"page": 1, "size": 20}
    assert target.make_page(page=2, size=50) == {"page": 2, "size": 50}


def test_pick_option() -> None:
    assert target.pick_option({"timeout": 10}, "timeout", 3) == 10
    assert target.pick_option({}, "timeout", 3) == 3
