from importlib import import_module

webhook = import_module("exercises.webhooks.01_webhook_security")


def test_sign_and_verify_payload() -> None:
    payload = b'{"event":"created"}'
    signature = webhook.sign_payload("secret", payload)

    assert webhook.verify_signature("secret", payload, signature) is True
    assert webhook.verify_signature("secret", payload, "bad") is False


def test_should_process_rejects_empty_and_duplicate_event() -> None:
    assert webhook.should_process("", set()) is False
    assert webhook.should_process("evt-1", {"evt-1"}) is False
    assert webhook.should_process("evt-2", {"evt-1"}) is True
