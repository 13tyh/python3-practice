"""MongoDB index / upsert の練習。"""


def single_index(field: str, descending: bool = False) -> list[tuple[str, int]]:
    # TODO
    raise NotImplementedError


def compound_index(fields: list[str]) -> list[tuple[str, int]]:
    # TODO
    raise NotImplementedError


def build_upsert_update(data: dict[str, object]) -> dict[str, dict[str, object]]:
    # TODO
    raise NotImplementedError


def explain_uses_index(explain: dict[str, object]) -> bool:
    # TODO
    raise NotImplementedError

