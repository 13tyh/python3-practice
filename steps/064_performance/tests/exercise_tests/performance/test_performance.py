from importlib import import_module

target = import_module("exercises.performance.01_performance")


def test_performance() -> None:
    assert list(target.iter_csv_lines(["a,b", "c,d"])) == [["a", "b"], ["c", "d"]]
    assert list(target.chunk_items([1, 2, 3], 2)) == [[1, 2], [3]]
    result, elapsed = target.measure_elapsed(lambda: "ok")
    assert result == "ok"
    assert elapsed >= 0
