"""tool calling contractの練習。"""

from typing import Any


def is_allowed_tool(tool_name: str, allowed_tools: set[str]) -> bool:
    """tool_nameがallowlistにあればTrue。"""
    # TODO
    raise NotImplementedError


def missing_arguments(arguments: dict[str, Any], required: set[str]) -> list[str]:
    """tool argumentsの不足keyを返す。"""
    # TODO
    raise NotImplementedError


def validate_tool_call(call: dict[str, Any], allowed_tools: set[str], required: set[str]) -> bool:
    """tool名とargumentsが妥当ならTrue。"""
    # TODO
    raise NotImplementedError
