from importlib import import_module

import pytest

target = import_module("exercises.core_design_thinking.04_state_transition")


def test_state_transition() -> None:
    assert target.can_transition("draft", "submitted")
    assert not target.can_transition("draft", "published")
    assert target.transition("submitted", "approved") == "approved"
    with pytest.raises(ValueError):
        target.transition("published", "draft")
