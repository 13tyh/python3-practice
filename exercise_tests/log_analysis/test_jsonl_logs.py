import json
from importlib import import_module
from pathlib import Path

target = import_module("exercises.log_analysis.01_jsonl_logs")


def test_jsonl_logs(tmp_path: Path) -> None:
    path = tmp_path / "app.jsonl"
    logs = [
        {"action": "review", "status": "ok", "elapsed_ms": 100},
        {"action": "review", "status": "error", "elapsed_ms": 300},
        {"action": "chat", "status": "ok", "elapsed_ms": 200},
    ]
    path.write_text("\n".join(json.dumps(row) for row in logs) + "\n", encoding="utf-8")
    loaded = target.read_jsonl_logs(path)
    assert loaded == logs
    assert target.error_rate(loaded) == 1 / 3
    assert target.average_elapsed_ms(loaded) == 200
    assert target.count_by_action(loaded) == {"review": 2, "chat": 1}
