"""GitHub Actionsのログを読む練習。"""


def failed_steps(log: str) -> list[str]:
    """`##[error]Process completed...` の直前にある `Run ...` 行を返す。"""
    # TODO
    raise NotImplementedError


def pytest_failures(log: str) -> list[str]:
    """pytestの `FAILED path::test_name` 行だけを返す。"""
    # TODO
    raise NotImplementedError
