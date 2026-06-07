from importlib import import_module

target = import_module("exercises.ai_safety_filters.01_safety")


def test_mask_email() -> None:
    assert target.mask_email("contact aki@example.com") == "contact [EMAIL]"


def test_unsafe_reasons() -> None:
    assert target.unsafe_reasons("please delete database") == ["delete database"]


def test_safety_decision() -> None:
    assert target.safety_decision("hello") == {"allow": True, "reasons": []}
    assert target.safety_decision("steal token") == {"allow": False, "reasons": ["steal token"]}
