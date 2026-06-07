"""fixed window rate limitの練習。"""


def count_in_window(timestamps: list[int], now: int, window_seconds: int) -> int:
    """window内のrequest数を数える。"""
    # TODO
    raise NotImplementedError


def is_allowed(timestamps: list[int], now: int, limit: int, window_seconds: int) -> bool:
    """window内のrequest数がlimit未満ならTrue。"""
    # TODO
    raise NotImplementedError


def retry_after_seconds(timestamps: list[int], now: int, window_seconds: int) -> int:
    """一番古いrequestがwindow外へ出るまでの秒数を返す。"""
    # TODO
    raise NotImplementedError
