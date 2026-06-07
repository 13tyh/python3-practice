"""MongoDB migration 的処理の練習。"""


def add_default_field(documents: list[dict[str, object]], field: str, default: object) -> list[dict[str, object]]:
    # TODO
    raise NotImplementedError


def rename_field(document: dict[str, object], old: str, new: str) -> dict[str, object]:
    # TODO
    raise NotImplementedError


def migration_update_many_filter(field: str) -> dict[str, object]:
    """field が存在しない document を探す filter。"""
    # TODO
    raise NotImplementedError

