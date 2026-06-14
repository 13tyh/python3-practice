from exercises.basics_repetition.round_25 import build_error, ok_response, validate_response


def test_round_25() -> None:
    assert build_error("bad_request", "invalid") == {"code": "bad_request", "message": "invalid"}
    assert ok_response({"id": 1}) == {"ok": True, "data": {"id": 1}}
    assert validate_response({"ok": True, "data": {}})
    assert validate_response({"ok": False, "error": {"code": "x", "message": "ng"}})
    assert not validate_response({"data": {}})
