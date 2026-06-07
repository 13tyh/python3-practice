from importlib import import_module
from multiprocessing import Queue

target = import_module("exercises.processes.02_multiprocessing")


def test_square() -> None:
    assert target.square(4) == 16


def test_square_all() -> None:
    assert target.square_all([1, 2, 3]) == [1, 4, 9]


def test_worker_put_square() -> None:
    queue: Queue[int] = Queue()
    target.worker_put_square(5, queue)
    assert queue.get(timeout=1) == 25


def test_split_chunks() -> None:
    assert target.split_chunks([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

