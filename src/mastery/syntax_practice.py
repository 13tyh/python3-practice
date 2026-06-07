from __future__ import annotations


def normalize_name(name: str) -> str:
    """Trim spaces and convert a name to title case."""
    return name.strip().title()


def calculate_total(prices: list[int], tax_rate: float) -> int:
    """Return rounded total price including tax."""
    subtotal = sum(prices)
    return round(subtotal * (1 + tax_rate))


def find_user_email(users: list[dict[str, str]], user_id: str) -> str:
    """Find a user's email by id.

    Raise ValueError when the user is not found.
    """
    for user in users:
        if user.get("id") == user_id:
            return user["email"]
    raise ValueError(f"user not found: {user_id}")

