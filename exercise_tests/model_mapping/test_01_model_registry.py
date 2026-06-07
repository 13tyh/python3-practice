from importlib import import_module

target = import_module("exercises.model_mapping.01_model_registry")


def test_model_registry() -> None:
    items = [
        target.ModelDeployment("chat-prod", "gpt-4.1", "azure", "prod"),
        target.ModelDeployment("chat-dev", "gpt-4.1-mini", "azure", "dev"),
        target.ModelDeployment("gemini-prod", "gemini-2.5-flash", "vertex", "prod"),
    ]
    assert target.find_model_name(items, "chat-prod") == "gpt-4.1"
    assert target.find_deployment_name(items, "gpt-4.1-mini", "dev") == "chat-dev"
    assert target.group_by_provider(items) == {
        "azure": ["chat-prod", "chat-dev"],
        "vertex": ["gemini-prod"],
    }
    assert target.build_model_log_context(items[0]) == {
        "deployment_name": "chat-prod",
        "model_name": "gpt-4.1",
        "provider": "azure",
        "environment": "prod",
    }

