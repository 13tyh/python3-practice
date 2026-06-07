"""特化型AIの要件定義練習。"""

REQUIRED_FIELDS = {"domain", "users", "tasks", "success_metrics", "out_of_scope"}


def missing_requirement_fields(requirements: dict[str, object]) -> list[str]:
    """特化型AI要件として不足している項目を返す。"""
    # TODO
    raise NotImplementedError


def is_in_scope(task: str, allowed_tasks: list[str], out_of_scope: list[str]) -> bool:
    """taskがallowedに含まれ、out_of_scopeに含まれなければTrue。"""
    # TODO
    raise NotImplementedError


def ai_fit_reason(task_type: str) -> str:
    """task_typeからAI化の向き不向きを短く返す。"""
    # TODO
    raise NotImplementedError
