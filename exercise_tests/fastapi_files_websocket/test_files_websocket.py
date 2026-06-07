from importlib import import_module

target = import_module("exercises.fastapi_files_websocket.01_files_websocket")


def test_is_allowed_upload() -> None:
    assert target.is_allowed_upload("report.pdf", "application/pdf", 100, 1000)
    assert not target.is_allowed_upload("report.exe", "application/octet-stream", 100, 1000)
    assert not target.is_allowed_upload("report.pdf", "application/pdf", 2000, 1000)


def test_safe_upload_name() -> None:
    assert target.safe_upload_name("../secret.txt") == "secret.txt"
    assert target.safe_upload_name("docs/report.pdf") == "report.pdf"


def test_build_ws_message() -> None:
    assert target.build_ws_message("progress", {"done": 1}) == {
        "event": "progress",
        "payload": {"done": 1},
    }
