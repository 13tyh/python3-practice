"""RAG 用 prompt 作成。"""


def build_rag_prompt(question: str, context: str) -> str:
    # TODO
    raise NotImplementedError


def refusal_message() -> str:
    # TODO
    raise NotImplementedError


def answer_from_context(question: str, context: str) -> str:
    """context が空なら回答拒否メッセージ。"""
    # TODO
    raise NotImplementedError
