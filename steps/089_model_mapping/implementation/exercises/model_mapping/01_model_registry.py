"""deployment_name と model_name のマッピング練習。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelDeployment:
    deployment_name: str
    model_name: str
    provider: str
    environment: str


def find_model_name(deployments: list[ModelDeployment], deployment_name: str) -> str:
    # TODO
    raise NotImplementedError


def find_deployment_name(
    deployments: list[ModelDeployment],
    model_name: str,
    environment: str,
) -> str:
    # TODO
    raise NotImplementedError


def group_by_provider(deployments: list[ModelDeployment]) -> dict[str, list[str]]:
    """provider ごとに deployment_name を集める。"""
    # TODO
    raise NotImplementedError


def build_model_log_context(deployment: ModelDeployment) -> dict[str, str]:
    # TODO
    raise NotImplementedError
