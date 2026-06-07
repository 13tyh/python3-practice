"""AI client boundary.

実サービスでは LangChain / GenAI / Vertex AI などをこの層に閉じ込める。
router や service からSDK詳細を直接触らないための境界。
"""


class LocalAiClient:
    """テスト用の最小AI client。"""

    def __init__(self, prefix: str = "fake response") -> None:
        self.prefix = prefix

    def invoke(self, prompt: str) -> str:
        """promptから応答文字列を返す。"""
        # TODO
        raise NotImplementedError


def build_ai_client(provider: str) -> LocalAiClient:
    """provider名からAI clientを作る。"""
    # TODO
    raise NotImplementedError
