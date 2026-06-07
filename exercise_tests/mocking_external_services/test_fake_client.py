from importlib import import_module

import pytest

target = import_module("exercises.mocking_external_services.01_fake_client")


def test_fake_client_records_calls() -> None:
    client = target.FakeHttpClient({"/users/u1": {"name": "Aki"}})

    assert target.fetch_user_name(client, "u1") == "Aki"
    assert client.calls == ["/users/u1"]


def test_fake_client_rejects_unknown_url() -> None:
    client = target.FakeHttpClient({})

    with pytest.raises(KeyError):
        client.get("/missing")
