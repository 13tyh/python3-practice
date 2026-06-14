from importlib import import_module

target = import_module("exercises.domain_guardrails.01_policy")


def test_is_domain_allowed() -> None:
    assert target.is_domain_allowed("municipality") is True
    assert target.is_domain_allowed("medical") is False


def test_policy_violations() -> None:
    assert target.policy_violations("password と マイナンバー") == ["credential", "pii"]


def test_refusal_message() -> None:
    assert target.refusal_message("out_of_scope") == "対象業務外のため回答できません。"
