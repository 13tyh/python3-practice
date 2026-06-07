"""会話memoryをtrimする練習。"""

Message = dict[str, str]


def count_by_role(messages: list[Message]) -> dict[str, int]:
    """roleごとのmessage数を返す。"""
    # TODO
    raise NotImplementedError


def trim_messages(messages: list[Message], max_chars: int) -> list[Message]:
    """systemを保持し、末尾優先でmax_chars以内にする。"""
    # TODO
    raise NotImplementedError


def memory_summary(messages: list[Message]) -> str:
    """message数とrole数を含むsummaryを返す。"""
    # TODO
    raise NotImplementedError
