from importlib import import_module
from pathlib import Path

target = import_module("exercises.batch_inference.01_batch_input")


def test_build_prompt_record() -> None:
    assert target.build_prompt_record("1", "hello") == {
        "id": "1",
        "request": {"contents": [{"role": "user", "parts": [{"text": "hello"}]}]},
    }


def test_jsonl(tmp_path: Path) -> None:
    records = [target.build_prompt_record("1", "hello"), target.build_prompt_record("2", "bye")]
    text = target.to_jsonl(records)
    assert len(text.splitlines()) == 2
    path = tmp_path / "input.jsonl"
    target.write_jsonl(path, records)
    assert target.read_jsonl(path) == records
