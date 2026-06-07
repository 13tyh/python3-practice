"""transaction の考え方。"""


class FakeTransaction:
    def __init__(self) -> None:
        self.committed = False
        self.rolled_back = False

    def commit(self) -> None:
        self.committed = True

    def rollback(self) -> None:
        self.rolled_back = True


def run_in_transaction(tx: FakeTransaction, should_fail: bool) -> str:
    # TODO
    raise NotImplementedError


def should_use_transaction(operations_count: int, writes_multiple_resources: bool) -> bool:
    # TODO
    raise NotImplementedError

