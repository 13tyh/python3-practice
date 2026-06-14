"""webhook署名検証とidempotencyの練習。"""


def sign_payload(secret: str, payload: bytes) -> str:
    """HMAC-SHA256のhex digestを返す。"""
    # TODO
    raise NotImplementedError


def verify_signature(secret: str, payload: bytes, signature: str) -> bool:
    """署名を安全に比較する。"""
    # TODO
    raise NotImplementedError


def should_process(event_id: str, processed_ids: set[str]) -> bool:
    """未処理eventだけTrueを返す。空IDは処理しない。"""
    # TODO
    raise NotImplementedError
