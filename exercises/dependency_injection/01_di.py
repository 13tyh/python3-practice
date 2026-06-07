"""依存性注入の練習。"""

from typing import Protocol


class UserRepository(Protocol):
    def find_name(self, user_id: str) -> str | None:
        """Find user name."""


class DictUserRepository:
    def __init__(self, users: dict[str, str]) -> None:
        self.users = users

    def find_name(self, user_id: str) -> str | None:
        return self.users.get(user_id)


def greet_user(user_id: str, repository: UserRepository) -> str:
    # TODO
    raise NotImplementedError


def create_repository(users: dict[str, str]) -> UserRepository:
    # TODO
    raise NotImplementedError

