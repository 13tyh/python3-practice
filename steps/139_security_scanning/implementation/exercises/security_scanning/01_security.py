"""security scan / 権限漏れレビューの応用練習。"""


def mask_secret(value: str, visible: int = 4) -> str:
    """secretの末尾だけ見せてmaskする。"""
    # TODO
    raise NotImplementedError


def has_high_risk_vulnerability(vulnerabilities: list[dict[str, str]]) -> bool:
    """high/criticalの脆弱性があればTrue。"""
    # TODO
    raise NotImplementedError


def has_permission_leak(role: str, owner_id: str, user_id: str, action: str) -> bool:
    """viewerが他人のwriteをできるなら漏れ。"""
    # TODO
    raise NotImplementedError
