from exercises.basics_repetition.round_33 import create_resource, response_status, validate_payload


def test_round_33() -> None:
    assert validate_payload({"name": "Aki", "enabled": True}) == []
    assert validate_payload({"name": "", "enabled": "yes"}) == [
        "name is required",
        "enabled must be bool",
    ]
    assert create_resource({"name": "Aki"}, "r1") == {"id": "r1", "name": "Aki"}
    assert response_status({"ok": True}) == "ok"
    assert response_status({"ok": False}) == "error"
