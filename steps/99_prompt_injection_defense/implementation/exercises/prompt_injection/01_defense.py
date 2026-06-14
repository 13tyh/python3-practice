"""prompt injection防御の練習。"""

INJECTION_PATTERNS = ("ignore previous", "system prompt", "developer message", "指示を無視")


def injection_reasons(text: str) -> list[str]:
    """injection疑いのpatternを返す。"""
    # TODO
    raise NotImplementedError


def has_prompt_injection(text: str) -> bool:
    """injection疑いがあればTrue。"""
    # TODO
    raise NotImplementedError


def wrap_untrusted_context(context: str) -> str:
    """untrusted contextとして明示した文字列を返す。"""
    # TODO
    raise NotImplementedError
