"""LLM app の運用設計。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelCandidate:
    deployment_name: str
    model_name: str
    priority: int
    enabled: bool


def choose_model(candidates: list[ModelCandidate]) -> ModelCandidate:
    # TODO
    raise NotImplementedError


def prompt_key(name: str, version: str) -> str:
    # TODO
    raise NotImplementedError


def estimate_cost(input_tokens: int, output_tokens: int, price_per_1k: float) -> float:
    # TODO
    raise NotImplementedError


def passes_guardrails(text: str) -> bool:
    # TODO
    raise NotImplementedError
