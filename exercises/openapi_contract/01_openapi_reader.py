"""OpenAPI schemaを読む練習。"""


def paths_by_method(schema: dict[str, object], method: str) -> list[str]:
    """指定methodを持つpathを返す。"""
    # TODO
    raise NotImplementedError


def response_codes(schema: dict[str, object], path: str, method: str) -> list[str]:
    """path/methodのresponse code一覧を返す。"""
    # TODO
    raise NotImplementedError


def has_operation(schema: dict[str, object], path: str, method: str) -> bool:
    """operationが存在するか返す。"""
    # TODO
    raise NotImplementedError
