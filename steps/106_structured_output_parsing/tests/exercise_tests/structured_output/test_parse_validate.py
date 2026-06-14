from importlib import import_module

target = import_module("exercises.structured_output.01_parse_validate")


def test_parse_json_object() -> None:
    assert target.parse_json_object('{"answer": "ok"}') == {"answer": "ok"}
    assert target.parse_json_object("[1, 2]") is None
    assert target.parse_json_object("not json") is None


def test_missing_required_keys() -> None:
    assert target.missing_required_keys({"answer": "ok"}, {"answer", "citations"}) == ["citations"]


def test_is_valid_output() -> None:
    assert target.is_valid_output('{"answer": "ok"}', {"answer"}) is True
    assert target.is_valid_output('{"answer": "ok"}', {"answer", "citations"}) is False
