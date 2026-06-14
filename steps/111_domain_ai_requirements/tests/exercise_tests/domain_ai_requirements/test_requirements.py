from importlib import import_module

target = import_module("exercises.domain_ai_requirements.01_requirements")


def test_missing_requirement_fields() -> None:
    assert target.missing_requirement_fields({"domain": "自治体", "tasks": ["検索"]}) == [
        "out_of_scope",
        "success_metrics",
        "users",
    ]


def test_is_in_scope() -> None:
    assert target.is_in_scope("契約検索", ["契約検索"], ["個人情報推測"]) is True
    assert target.is_in_scope("個人情報推測", ["個人情報推測"], ["個人情報推測"]) is False


def test_ai_fit_reason() -> None:
    assert target.ai_fit_reason("faq") == "good: knowledge retrieval"
    assert target.ai_fit_reason("payment") == "bad: deterministic transaction"
