from typing import Protocol


class AIClient(Protocol):
    def review(self, code: str, focus: str) -> str:
        """Return review text."""


class FakeAIClient:
    def review(self, code: str, focus: str) -> str:
        return f"{focus}: check error handling\nadd tests"

