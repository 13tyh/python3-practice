"""AI dataset versioning / annotationの応用練習。"""


def dataset_fingerprint(records: list[dict[str, object]]) -> str:
    """recordsから安定したfingerprintを返す。"""
    # TODO
    raise NotImplementedError


def unreviewed_ids(records: list[dict[str, object]]) -> list[str]:
    """reviewedがFalseのrecord idを返す。"""
    # TODO
    raise NotImplementedError


def label_distribution(records: list[dict[str, str]]) -> dict[str, int]:
    """labelごとの件数を返す。"""
    # TODO
    raise NotImplementedError
