"""解答例: exercises/basics/01_values.py."""


def make_profile(name: str, age: int) -> str:
    return f"{name} is {age} years old"


def yen_to_text(amount: int) -> str:
    return f"{amount}円"


def minutes_to_seconds(minutes: int) -> int:
    return minutes * 60


def add_tax(price: int, tax_rate: float) -> int:
    return round(price * (1 + tax_rate))
