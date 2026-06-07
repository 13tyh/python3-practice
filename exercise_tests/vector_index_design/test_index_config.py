from importlib import import_module

import pytest

target = import_module("exercises.vector_index_design.01_index_config")


def test_normalize_metric() -> None:
    assert target.normalize_metric("Cosine") == "cosine"

    with pytest.raises(ValueError):
        target.normalize_metric("unknown")


def test_validate_dimension() -> None:
    assert target.validate_dimension([0.1, 0.2], 2) is True
    assert target.validate_dimension([0.1], 2) is False


def test_build_index_config() -> None:
    assert target.build_index_config(768, "cosine", ["city_id"]) == {
        "dimension": 768,
        "metric": "cosine",
        "filter_fields": ["city_id"],
    }
