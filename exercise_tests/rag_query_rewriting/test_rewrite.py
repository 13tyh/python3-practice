from importlib import import_module

target = import_module("exercises.rag_query_rewriting.01_rewrite")


def test_normalize_query() -> None:
    assert target.normalize_query("  Python   API ") == "python api"


def test_expand_query() -> None:
    assert target.expand_query("自治体 契約") == [
        "自治体",
        "契約",
        "市区町村",
        "municipality",
        "subscription",
    ]


def test_extract_metadata_filter() -> None:
    assert target.extract_metadata_filter("city:tokyo plan:pro 契約") == {
        "city": "tokyo",
        "plan": "pro",
    }
