from importlib import import_module

target = import_module("exercises.ai_dataset_versioning.01_dataset")


def test_dataset_fingerprint_is_stable() -> None:
    left = [{"id": "1", "text": "hello"}]
    right = [{"text": "hello", "id": "1"}]

    assert target.dataset_fingerprint(left) == target.dataset_fingerprint(right)


def test_unreviewed_ids() -> None:
    records = [{"id": "a", "reviewed": False}, {"id": "b", "reviewed": True}]

    assert target.unreviewed_ids(records) == ["a"]


def test_label_distribution() -> None:
    records = [{"label": "good"}, {"label": "bad"}, {"label": "good"}]

    assert target.label_distribution(records) == {"good": 2, "bad": 1}
