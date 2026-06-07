"""例外設計の応用。"""


class DomainError(Exception):
    pass


class NotFoundError(DomainError):
    pass


class ValidationError(DomainError):
    pass


def require_non_empty(value: str, field_name: str) -> str:
    # TODO
    raise NotImplementedError


def find_required(data: dict[str, str], key: str) -> str:
    # TODO
    raise NotImplementedError

