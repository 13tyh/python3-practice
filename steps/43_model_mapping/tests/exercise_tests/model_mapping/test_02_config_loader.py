import json
from importlib import import_module

target = import_module("exercises.model_mapping.02_config_loader")


def test_config_loader(monkeypatch) -> None:
    text = json.dumps(
        [
            {
                "deployment_name": "chat-prod",
                "model_name": "gpt-4.1",
                "provider": "azure",
                "environment": "prod",
            }
        ]
    )
    parsed = target.parse_deployment_json(text)
    assert parsed[0].deployment_name == "chat-prod"
    monkeypatch.setenv("MODEL_DEPLOYMENTS", text)
    assert target.load_deployments_from_env()[0].model_name == "gpt-4.1"


def test_validate_unique_deployment_names() -> None:
    deployment = import_module("exercises.model_mapping.01_model_registry").ModelDeployment
    items = [
        deployment("a", "m1", "azure", "prod"),
        deployment("a", "m2", "azure", "dev"),
        deployment("b", "m3", "vertex", "prod"),
    ]
    assert target.validate_unique_deployment_names(items) == ["duplicate deployment_name: a"]
