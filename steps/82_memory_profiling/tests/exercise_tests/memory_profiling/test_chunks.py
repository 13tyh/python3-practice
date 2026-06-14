from importlib import import_module

import pytest

target = import_module("exercises.memory_profiling.01_chunks")


def test_chunked() -> None:
    assert target.chunked([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunked_rejects_invalid_size() -> None:
    with pytest.raises(ValueError):
        target.chunked([1], 0)


def test_estimate_rows_per_chunk() -> None:
    assert target.estimate_rows_per_chunk(memory_limit_mb=1, bytes_per_row=1024) == 1024
