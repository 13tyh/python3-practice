"""MongoDB運用とschema設計の応用練習。"""


def recommended_index(query_fields: list[str], sort_fields: list[str]) -> list[tuple[str, int]]:
    """query条件を先、sort条件を後にしたcompound indexを返す。"""
    # TODO
    raise NotImplementedError


def build_required_schema(required_fields: list[str]) -> dict[str, object]:
    """requiredだけを持つ簡易schema validation設定を返す。"""
    # TODO
    raise NotImplementedError


def is_slow_query(explain: dict[str, int], max_docs_examined: int) -> bool:
    """docsExaminedが多すぎるqueryならTrue。"""
    # TODO
    raise NotImplementedError
