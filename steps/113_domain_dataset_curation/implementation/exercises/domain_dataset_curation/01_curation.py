"""特化型AIデータ整備の練習。"""

Example = dict[str, str]


def valid_examples(examples: list[Example]) -> list[Example]:
    """question/answerが空でない例だけ返す。"""
    # TODO
    raise NotImplementedError


def deduplicate_examples(examples: list[Example]) -> list[Example]:
    """questionが重複する例を先勝ちで除外する。"""
    # TODO
    raise NotImplementedError


def split_eval_ids(examples: list[Example], eval_every: int) -> list[str]:
    """deterministicにevalへ回すexample idを返す。"""
    # TODO
    raise NotImplementedError
