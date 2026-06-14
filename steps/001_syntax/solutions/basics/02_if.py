"""解答例: exercises/basics/02_if.py."""


def judge_age(age: int) -> str:
    return "adult" if age >= 18 else "minor"


def max_number(a: int, b: int) -> int:
    return a if a >= b else b


def shipping_fee(total: int, area: str) -> int:
    threshold = 8000 if area in {"北海道", "沖縄"} else 5000
    return 0 if total >= threshold else 500


def password_strength(password: str) -> str:
    if len(password) < 8:
        return "weak"
    if any(char.isdigit() for char in password):
        return "strong"
    return "normal"
