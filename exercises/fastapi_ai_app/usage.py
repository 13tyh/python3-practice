"""AI token usage / cost tracking."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TokenUsage:
    input_tokens: int
    output_tokens: int
    model_name: str


def total_tokens(usage: TokenUsage) -> int:
    # TODO
    raise NotImplementedError


def estimate_cost_usd(usage: TokenUsage, price_per_1k_tokens: float) -> float:
    # TODO
    raise NotImplementedError


def usage_log_context(usage: TokenUsage) -> dict[str, str]:
    # TODO
    raise NotImplementedError
