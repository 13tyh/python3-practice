"""FastAPI file upload / WebSocketの応用練習。"""


def is_allowed_upload(filename: str, content_type: str, size_bytes: int, max_size: int) -> bool:
    """拡張子、content type、sizeからupload可否を返す。"""
    # TODO
    raise NotImplementedError


def safe_upload_name(filename: str) -> str:
    """path traversalを避けるためファイル名だけを返す。"""
    # TODO
    raise NotImplementedError


def build_ws_message(event: str, payload: dict[str, object]) -> dict[str, object]:
    """WebSocketで送るmessage形式を作る。"""
    # TODO
    raise NotImplementedError
