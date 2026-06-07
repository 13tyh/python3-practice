"""既存Mongo documentに新fieldを足すmigration練習。"""


def needs_backfill(document: dict[str, object], field: str) -> bool:
    """fieldが存在しないdocumentだけbackfill対象にする。"""
    # TODO
    raise NotImplementedError


def build_set_update(field: str, default: object) -> dict[str, dict[str, object]]:
    """Mongoの `$set` update payloadを作る。"""
    # TODO
    raise NotImplementedError


def migration_summary(documents: list[dict[str, object]], field: str) -> dict[str, int]:
    """全件数とbackfill対象件数を返す。"""
    # TODO
    raise NotImplementedError
