from typing import Protocol

from .model import Review


class ReviewRepository(Protocol):
    def save(self, review: Review) -> None:
        """Save review."""

    def list_reviews(self) -> list[Review]:
        """List reviews."""


class InMemoryReviewRepository:
    def __init__(self) -> None:
        self._items: list[Review] = []

    def save(self, review: Review) -> None:
        self._items.append(review)

    def list_reviews(self) -> list[Review]:
        return list(self._items)
