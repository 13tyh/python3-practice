"""prompt templateの練習。"""


def missing_variables(template: str, values: dict[str, str]) -> list[str]:
    """template内の変数のうちvaluesにないものを返す。"""
    # TODO
    raise NotImplementedError


def render_template(template: str, values: dict[str, str]) -> str:
    """不足変数がなければformatして返す。"""
    # TODO
    raise NotImplementedError


def build_messages(
    system_template: str, user_template: str, values: dict[str, str]
) -> list[dict[str, str]]:
    """system/user messageを分けて返す。"""
    # TODO
    raise NotImplementedError
