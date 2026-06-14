"""特化型AI guardrails policyの練習。"""

ALLOWED_DOMAINS = {"municipality", "subscription", "group", "user"}
POLICY_KEYWORDS = {"pii": ["マイナンバー", "ssn"], "credential": ["password", "api key"]}


def is_domain_allowed(domain: str) -> bool:
    """許可されたdomainならTrue。"""
    # TODO
    raise NotImplementedError


def policy_violations(text: str) -> list[str]:
    """textに含まれるpolicy違反カテゴリを返す。"""
    # TODO
    raise NotImplementedError


def refusal_message(reason: str) -> str:
    """安全な拒否文を返す。"""
    # TODO
    raise NotImplementedError
