"""Google Gen AI / Vertex AI の設定練習。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GenAISettings:
    model: str
    api_key: str | None
    use_vertexai: bool
    project: str | None
    location: str


def load_settings(model: str = "gemini-2.5-flash") -> GenAISettings:
    """環境変数から設定を読む。API key は必須にしない。"""
    # TODO
    raise NotImplementedError


def choose_auth_mode(settings: GenAISettings) -> str:
    """vertex / api_key / missing のどれかを返す。"""
    # TODO
    raise NotImplementedError


def build_prompt(task: str, code: str) -> str:
    """AIに渡すレビュー用プロンプトを作る。"""
    # TODO
    raise NotImplementedError


def extract_text(response: object) -> str:
    """response.text があれば文字列として返す。なければ空文字。"""
    # TODO
    raise NotImplementedError


def mask_secret(value: str | None) -> str:
    """ログ表示用に secret を隠す。"""
    # TODO
    raise NotImplementedError
