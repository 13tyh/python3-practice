from importlib import import_module

target = import_module("exercises.domain_dataset_curation.01_curation")


def test_valid_examples() -> None:
    examples = [
        {"id": "1", "question": "q", "answer": "a"},
        {"id": "2", "question": "", "answer": "a"},
    ]

    assert target.valid_examples(examples) == [examples[0]]


def test_deduplicate_examples() -> None:
    examples = [
        {"id": "1", "question": "q", "answer": "a"},
        {"id": "2", "question": "q", "answer": "b"},
    ]

    assert target.deduplicate_examples(examples) == [examples[0]]


def test_split_eval_ids() -> None:
    examples = [{"id": str(index), "question": "q", "answer": "a"} for index in range(1, 6)]

    assert target.split_eval_ids(examples, eval_every=2) == ["2", "4"]
