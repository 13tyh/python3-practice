"""悪い例: 型ヒントが実態と違う。"""


def find_user_email(users: list[dict[str, str]], user_id: str) -> str:
    for user in users:
        if user["id"] == user_id:
            return user["email"]
    return None  # type: ignore[return-value]


def load_count() -> int:
    return "10"  # type: ignore[return-value]

