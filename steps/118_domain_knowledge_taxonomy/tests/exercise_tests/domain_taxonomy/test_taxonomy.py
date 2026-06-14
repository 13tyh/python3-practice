from importlib import import_module

target = import_module("exercises.domain_taxonomy.01_taxonomy")


def test_normalize_label() -> None:
    assert target.normalize_label(" 自治体 ") == "municipality"
    assert target.normalize_label("Group") == "group"


def test_is_allowed_category() -> None:
    assert target.is_allowed_category("契約") is True
    assert target.is_allowed_category("unknown") is False


def test_canonical_terms() -> None:
    assert target.canonical_terms(["自治体", "municipality", "契約"]) == [
        "municipality",
        "subscription",
    ]
