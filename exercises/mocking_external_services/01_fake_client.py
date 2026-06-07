"""外部APIをfake clientで置き換える練習。"""


class FakeHttpClient:
    def __init__(self, responses: dict[str, dict[str, object]]) -> None:
        self.responses = responses
        self.calls: list[str] = []

    def get(self, url: str) -> dict[str, object]:
        """call履歴を残し、登録済みresponseを返す。"""
        # TODO
        raise NotImplementedError


def fetch_user_name(client: FakeHttpClient, user_id: str) -> str:
    """fake client経由でuser名を返す。"""
    # TODO
    raise NotImplementedError
