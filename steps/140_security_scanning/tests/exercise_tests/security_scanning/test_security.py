from importlib import import_module

target = import_module("exercises.security_scanning.01_security")


def test_mask_secret() -> None:
    assert target.mask_secret("sk-abcdef") == "*****cdef"


def test_has_high_risk_vulnerability() -> None:
    vulns = [{"package": "x", "severity": "critical"}]

    assert target.has_high_risk_vulnerability(vulns)
    assert not target.has_high_risk_vulnerability([{"severity": "low"}])


def test_has_permission_leak() -> None:
    assert target.has_permission_leak("viewer", "owner-1", "user-2", "write")
    assert not target.has_permission_leak("admin", "owner-1", "user-2", "write")
