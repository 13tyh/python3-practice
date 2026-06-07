from importlib import import_module

target = import_module("exercises.finetuning_dataset_prep.01_prep")


def test_training_record() -> None:
    record = target.training_record("rules", "question", "answer")

    assert record["messages"][0] == {"role": "system", "content": "rules"}
    assert record["messages"][2] == {"role": "assistant", "content": "answer"}


def test_has_required_roles() -> None:
    record = target.training_record("rules", "question", "answer")

    assert target.has_required_roles(record) is True
    assert target.has_required_roles({"messages": [{"role": "user", "content": "q"}]}) is False


def test_to_jsonl_line() -> None:
    assert target.to_jsonl_line({"a": 1}) == '{"a": 1}'
