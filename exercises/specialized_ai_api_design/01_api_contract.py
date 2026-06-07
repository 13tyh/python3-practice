"""特化型AI API設計の練習。"""


def validate_request(payload: dict[str, object]) -> list[str]:
    """question/domain/user_idの不足keyを返す。"""
    # TODO
    raise NotImplementedError


def response_skeleton(status: str) -> dict[str, object]:
    """answer/citations/decisionを含むresponse skeletonを返す。"""
    # TODO
    raise NotImplementedError


def decision_status(answerable: bool, blocked: bool) -> str:
    """answerable/blockedからstatusを返す。"""
    # TODO
    raise NotImplementedError
