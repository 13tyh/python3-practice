"""環境変数から model mapping を読む練習。"""

from __future__ import annotations

import json
import os
from importlib import import_module

ModelDeployment = import_module("exercises.model_mapping.01_model_registry").ModelDeployment


def parse_deployment_json(text: str) -> list[ModelDeployment]:
    # TODO
    raise NotImplementedError


def load_deployments_from_env(env_name: str = "MODEL_DEPLOYMENTS") -> list[ModelDeployment]:
    # TODO
    raise NotImplementedError


def validate_unique_deployment_names(deployments: list[ModelDeployment]) -> list[str]:
    # TODO
    raise NotImplementedError
