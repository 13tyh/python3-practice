from importlib import import_module

import pytest
from pydantic import ValidationError

target = import_module("exercises.pydantic_validation.01_validation")


def test_pydantic_validation() -> None:
    user = target.CreateUser(
        email="aki@example.com",
        role="admin",
        profile={"display_name": "Aki"},
    )
    assert target.create_user_label(user) == "Aki <aki@example.com> admin"
    with pytest.raises(ValidationError):
        target.CreateUser(email="invalid", role="member", profile={"display_name": "Ren"})

