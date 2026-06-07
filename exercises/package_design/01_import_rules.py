"""package design の考え方。"""


def is_private_name(name: str) -> bool:
    # TODO
    raise NotImplementedError


def public_api_names(names: list[str]) -> list[str]:
    # TODO
    raise NotImplementedError


def is_allowed_import(from_layer: str, to_layer: str) -> bool:
    """router -> service -> repository の向きだけ許可する。"""
    # TODO
    raise NotImplementedError

