"""Docker運用で見るenvとhealthcheckの練習。"""

from collections.abc import Mapping

REQUIRED_ENV = ("APP_ENV", "MONGO_URI")


def missing_required_env(env: Mapping[str, str]) -> list[str]:
    """必須envのうち、存在しないか空文字のkeyを返す。"""
    # TODO
    raise NotImplementedError


def health_status(db_ok: bool, ai_ok: bool) -> dict[str, str]:
    """DB必須、AIはdegraded扱いでhealthを返す。"""
    # TODO
    raise NotImplementedError
