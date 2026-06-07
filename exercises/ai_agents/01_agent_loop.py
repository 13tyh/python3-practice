"""AI agent の最小構成。"""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class ToolCall:
    name: str
    args: dict[str, str]


AgentStep = Literal["plan", "tool", "answer", "human_review"]


def choose_next_step(message: str, tool_calls: list[ToolCall]) -> AgentStep:
    # TODO
    raise NotImplementedError


def validate_tool_call(call: ToolCall, allowed_tools: set[str]) -> bool:
    # TODO
    raise NotImplementedError


def update_memory(memory: list[str], message: str, limit: int) -> list[str]:
    # TODO
    raise NotImplementedError
