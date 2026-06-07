from fastapi.testclient import TestClient

from exercises.fastapi_app.main import create_app


def test_fastapi_task_flow() -> None:
    client = TestClient(create_app())

    assert client.get("/tasks").json() == []

    created = client.post("/tasks", json={"title": "learn typing", "minutes": 30})
    assert created.status_code == 201
    body = created.json()
    assert body == {"id": "task-1", "title": "learn typing", "minutes": 30, "done": False}

    assert client.get("/tasks").json() == [body]

    done = client.patch("/tasks/task-1/done")
    assert done.status_code == 200
    assert done.json()["done"] is True

    missing = client.patch("/tasks/missing/done")
    assert missing.status_code == 404
