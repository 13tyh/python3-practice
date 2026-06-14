from importlib import import_module

target = import_module("exercises.data_analysis_stats.01_stats")


def test_mean() -> None:
    assert target.mean([1, 2, 3]) == 2
    assert target.mean([]) == 0.0


def test_median() -> None:
    assert target.median([3, 1, 2]) == 2
    assert target.median([1, 2, 3, 4]) == 2.5


def test_find_outliers_iqr() -> None:
    assert target.find_outliers_iqr([10, 11, 12, 13, 100]) == [100]
