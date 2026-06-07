from dataclasses import dataclass
from importlib import import_module

target = import_module("exercises.typing_deep.02_protocol_generic")


@dataclass
class User:
    name: str


def test_protocol_generic() -> None:
    box = target.Box[int](123)
    assert box.get() == 123
    assert target.greet_named(User("Aki")) == "Hello, Aki"
    assert target.is_str_list(["a", "b"])
    assert not target.is_str_list(["a", 1])

