from importlib import import_module

target = import_module("exercises.basics.10_classes")


def test_total_price() -> None:
    books = [target.Book("A", 1000), target.Book("B", 1500)]
    assert target.total_price(books) == 2500


def test_counter() -> None:
    counter = target.Counter()
    assert counter.get() == 0
    counter.increment()
    counter.increment()
    assert counter.get() == 2
