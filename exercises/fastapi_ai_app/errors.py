"""FastAPI AI app の例外設計。"""


class AIAppError(Exception):
    status_code = 500


class AIUnavailableError(AIAppError):
    status_code = 502


class AIOutputError(AIAppError):
    status_code = 422


def error_to_response(error: AIAppError) -> dict[str, int | str]:
    # TODO
    raise NotImplementedError


def is_retryable(error: Exception) -> bool:
    # TODO
    raise NotImplementedError
