"""fine-tuning dataset準備の練習。"""


def training_record(system: str, user: str, assistant: str) -> dict[str, list[dict[str, str]]]:
    """chat形式のtraining recordを返す。"""
    # TODO
    raise NotImplementedError


def has_required_roles(record: dict[str, list[dict[str, str]]]) -> bool:
    """system/user/assistant roleが含まれていればTrue。"""
    # TODO
    raise NotImplementedError


def to_jsonl_line(record: dict[str, object]) -> str:
    """JSONL 1行に変換する。"""
    # TODO
    raise NotImplementedError
