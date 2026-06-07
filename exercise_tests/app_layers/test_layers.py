from exercises.app_layers.model import CreateStudyLogRequest, StudyLog
from exercises.app_layers.router import create_log_endpoint, next_action_endpoint, to_response
from exercises.app_layers.service import (
    create_study_log,
    suggest_next_action,
    total_minutes,
    validate_request,
)


def test_validate_request() -> None:
    assert validate_request(CreateStudyLogRequest("python", 30, "memo")) == []
    assert validate_request(CreateStudyLogRequest("", 0, "")) == [
        "topic is required",
        "minutes must be positive",
    ]


def test_create_study_log() -> None:
    log = create_study_log(CreateStudyLogRequest("python", 30, "memo"), "log-1")
    assert log == StudyLog("log-1", "python", 30, "memo")


def test_total_minutes() -> None:
    logs = [
        StudyLog("1", "python", 30, ""),
        StudyLog("2", "mongo", 20, ""),
        StudyLog("3", "python", 10, ""),
    ]
    assert total_minutes(logs) == 60
    assert total_minutes(logs, "python") == 40


def test_suggest_next_action() -> None:
    assert suggest_next_action([]) == "まずはPython基本を30分"
    logs = [StudyLog("1", "python", 40, "")]
    assert suggest_next_action(logs) == "pytestで確認する"
    logs.append(StudyLog("2", "api", 80, ""))
    assert suggest_next_action(logs) == "小さい機能を1つ実装する"


def test_to_response() -> None:
    response = to_response(StudyLog("1", "python", 30, "memo"))
    assert response.id == "1"
    assert response.title == "python: 30min"


def test_create_log_endpoint() -> None:
    result = create_log_endpoint({"topic": "python", "minutes": 30, "memo": "ok"}, "1")
    assert result == {"id": "1", "title": "python: 30min", "minutes": 30}


def test_next_action_endpoint() -> None:
    assert next_action_endpoint([]) == {"next_action": "まずはPython基本を30分"}

