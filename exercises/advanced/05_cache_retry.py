"""キャッシュとリトライの応用。"""

from collections.abc import Callable


def memoize_upper(text: str, cache: dict[str, str]) -> str:
    # TODO
    raise NotImplementedError


def retry_call(func: Callable[[], str], retries: int) -> str:
    # TODO
    raise NotImplementedError

