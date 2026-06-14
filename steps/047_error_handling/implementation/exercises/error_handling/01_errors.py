"""例外設計と HTTP error 変換。"""


class DomainError(Exception):
    status_code = 500


class BadRequestError(DomainError):
    status_code = 400


class NotFoundError(DomainError):
    status_code = 404


class ExternalServiceError(DomainError):
    status_code = 502


def to_http_error(error: DomainError) -> dict[str, int | str]:
    # TODO
    raise NotImplementedError


def should_retry(error: Exception) -> bool:
    # TODO
    raise NotImplementedError
