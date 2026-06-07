from __future__ import annotations

from typing import Any

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


def build_review_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            ("system", "あなたはPythonコードレビュー担当です。短く具体的に指摘します。"),
            ("human", "次のコードの問題点を3つ以内で挙げてください。\n{code}"),
        ]
    )


def build_review_chain(model: Any) -> Any:
    return build_review_prompt() | model | StrOutputParser()
