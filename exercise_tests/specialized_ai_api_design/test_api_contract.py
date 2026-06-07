from importlib import import_module

target = import_module("exercises.specialized_ai_api_design.01_api_contract")


def test_validate_request() -> None:
    assert target.validate_request({"question": "q", "domain": "municipality"}) == ["user_id"]


def test_response_skeleton() -> None:
    assert target.response_skeleton("answered") == {
        "status": "answered",
        "answer": "",
        "citations": [],
        "decision": {},
    }


def test_decision_status() -> None:
    assert target.decision_status(answerable=True, blocked=False) == "answered"
    assert target.decision_status(answerable=False, blocked=False) == "not_answerable"
    assert target.decision_status(answerable=True, blocked=True) == "blocked"
