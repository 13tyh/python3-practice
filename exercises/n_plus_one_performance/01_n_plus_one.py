"""N+1 問題の練習。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: str
    name: str


@dataclass(frozen=True)
class Order:
    id: str
    user_id: str
    amount: int


class FakeRepository:
    def __init__(self, users: list[User], orders: list[Order]) -> None:
        self.users = users
        self.orders = orders
        self.query_count = 0

    def list_orders(self) -> list[Order]:
        self.query_count += 1
        return self.orders

    def find_user(self, user_id: str) -> User | None:
        self.query_count += 1
        return next((user for user in self.users if user.id == user_id), None)

    def find_users_by_ids(self, user_ids: list[str]) -> list[User]:
        self.query_count += 1
        ids = set(user_ids)
        return [user for user in self.users if user.id in ids]


def list_order_rows_bad(repo: FakeRepository) -> list[dict[str, str | int | None]]:
    """悪い例: loop の中で user を1件ずつ取る。"""
    # TODO
    raise NotImplementedError


def list_order_rows_good(repo: FakeRepository) -> list[dict[str, str | int | None]]:
    """良い例: users をまとめて取って dict 化する。"""
    # TODO
    raise NotImplementedError


def user_map(users: list[User]) -> dict[str, User]:
    # TODO
    raise NotImplementedError

