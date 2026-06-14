"""Pydantic validation 深掘り。"""

from enum import Enum

from pydantic import BaseModel, Field, field_validator


class Role(str, Enum):
    admin = "admin"
    member = "member"


class Profile(BaseModel):
    display_name: str = Field(min_length=1)


class CreateUser(BaseModel):
    email: str
    role: Role
    profile: Profile

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        # TODO
        raise NotImplementedError


def create_user_label(user: CreateUser) -> str:
    # TODO
    raise NotImplementedError
