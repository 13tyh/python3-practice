from importlib import import_module

target = import_module("exercises.mongo_ops_schema.01_mongo_ops")


def test_recommended_index() -> None:
    assert target.recommended_index(["tenant_id", "status"], ["created_at"]) == [
        ("tenant_id", 1),
        ("status", 1),
        ("created_at", -1),
    ]


def test_build_required_schema() -> None:
    assert target.build_required_schema(["tenant_id", "name"]) == {
        "$jsonSchema": {"required": ["tenant_id", "name"]}
    }


def test_is_slow_query() -> None:
    assert target.is_slow_query({"totalDocsExamined": 5000}, 1000)
    assert not target.is_slow_query({"totalDocsExamined": 10}, 1000)
