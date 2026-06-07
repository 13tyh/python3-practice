"""基礎反復 round 32."""

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: str
    name: str
    role: str


def admin_users(users: list[User]) -> list[User]:
    # TODO
    raise NotImplementedError


def user_map(users: list[User]) -> dict[str, User]:
    # TODO
    raise NotImplementedError


def rename_user(user: User, name: str) -> User:
    # TODO
    raise NotImplementedError
