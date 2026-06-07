from importlib import import_module

target = import_module("exercises.basics.28_decorators")


def test_decorator_tasks() -> None:
    @target.add_prefix("hello ")
    def name() -> str:
        return "Aki"

    assert name() == "hello Aki"

    @target.call_twice
    def value() -> str:
        return "x"

    assert value() == ["x", "x"]

    @target.safe_return("fallback")
    def fail() -> str:
        raise RuntimeError("boom")

    assert fail() == "fallback"
