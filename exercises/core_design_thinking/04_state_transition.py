"""状態遷移の練習。"""

ALLOWED_TRANSITIONS = {
    "draft": {"submitted"},
    "submitted": {"approved", "rejected"},
    "approved": {"published"},
    "rejected": {"draft"},
    "published": set(),
}


def can_transition(current: str, next_status: str) -> bool:
    # TODO
    raise NotImplementedError


def transition(current: str, next_status: str) -> str:
    # TODO
    raise NotImplementedError

