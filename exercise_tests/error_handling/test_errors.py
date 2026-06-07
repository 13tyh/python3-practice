from importlib import import_module

target = import_module("exercises.error_handling.01_errors")


def test_errors() -> None:
    assert target.to_http_error(target.BadRequestError("bad")) == {"status_code": 400, "detail": "bad"}
    assert target.to_http_error(target.NotFoundError("missing")) == {
        "status_code": 404,
        "detail": "missing",
    }
    assert target.should_retry(target.ExternalServiceError("timeout"))
    assert not target.should_retry(target.BadRequestError("bad"))

