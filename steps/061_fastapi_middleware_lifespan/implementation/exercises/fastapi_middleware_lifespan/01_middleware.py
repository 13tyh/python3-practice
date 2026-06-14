"""FastAPI middleware / lifespanの応用練習。"""


def build_request_log(
    request_id: str, path: str, status_code: int, latency_ms: int
) -> dict[str, object]:
    """request log用のdictを作る。"""
    # TODO
    raise NotImplementedError


def should_enable_cors(origin: str, allowed_origins: list[str]) -> bool:
    """originが許可されているか判定する。"""
    # TODO
    raise NotImplementedError


def lifespan_event_order(resources: list[str]) -> list[str]:
    """接続は順番通り、切断は逆順のevent名を返す。"""
    # TODO
    raise NotImplementedError
