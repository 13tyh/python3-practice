"""自治体subscriptionを題材にdomain modelを作る練習。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Subscription:
    municipality_id: str
    plan: str
    seats: int
    active: bool


def can_add_user(subscription: Subscription, current_users: int) -> bool:
    """activeな契約で、seatに空きがある時だけTrue。"""
    # TODO
    raise NotImplementedError


def seats_by_municipality(subscriptions: list[Subscription]) -> dict[str, int]:
    """activeな契約だけを自治体IDごとに合計する。"""
    # TODO
    raise NotImplementedError
