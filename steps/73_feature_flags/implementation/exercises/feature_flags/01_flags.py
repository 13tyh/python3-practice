"""feature flagとrolloutの練習。"""


def rollout_bucket(user_id: str) -> int:
    """user_idから0-99の安定したbucketを返す。"""
    # TODO
    raise NotImplementedError


def is_enabled(flag: dict[str, object], user_id: str) -> bool:
    """enabledかつrollout_percent以内ならTrue。"""
    # TODO
    raise NotImplementedError
