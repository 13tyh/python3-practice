"""JWT / RBAC設計の応用練習。"""


def parse_bearer_token(header: str | None) -> str | None:
    """Authorization headerからBearer tokenを取り出す。"""
    # TODO
    raise NotImplementedError


def has_permission(role: str, action: str, permissions: dict[str, list[str]]) -> bool:
    """roleがactionを実行できるか返す。"""
    # TODO
    raise NotImplementedError


def build_claims(user_id: str, role: str, exp: int) -> dict[str, object]:
    """JWT payloadに入れるclaimを作る。"""
    # TODO
    raise NotImplementedError


def is_token_expired(now: int, exp: int) -> bool:
    """現在時刻がexp以上なら期限切れ。"""
    # TODO
    raise NotImplementedError
