"""デバッグ練習用。"""


def divide_scores(total: int, count: int) -> float:
    return total / count


def get_first_name(user: dict[str, str]) -> str:
    return user["name"].split()[0]


def parse_port(value: str) -> int:
    return int(value)
