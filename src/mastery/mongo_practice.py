from __future__ import annotations

import os
from typing import Any

from pymongo import MongoClient


def get_db() -> Any:
    uri = os.getenv("MONGO_URI", "mongodb://mongo:27017")
    client: MongoClient[Any] = MongoClient(uri)
    return client.python_master


def seed_users() -> None:
    db = get_db()
    db.users.delete_many({})
    db.users.insert_many(
        [
            {"name": "Aki", "role": "admin", "score": 92},
            {"name": "Ren", "role": "member", "score": 75},
            {"name": "Mio", "role": "member", "score": 88},
        ]
    )


def find_high_score_users(min_score: int) -> list[dict[str, Any]]:
    db = get_db()
    return list(db.users.find({"score": {"$gte": min_score}}, {"_id": 0}).sort("score", -1))

