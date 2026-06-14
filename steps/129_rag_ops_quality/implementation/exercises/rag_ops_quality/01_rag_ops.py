"""RAG運用品質の応用練習。"""


def needs_reindex(document_updated_at: str, index_updated_at: str) -> bool:
    """document更新がindex更新より新しければTrue。ISO文字列前提。"""
    # TODO
    raise NotImplementedError


def search_click_rate(logs: list[dict[str, object]]) -> float:
    """検索結果がclickされた割合を返す。"""
    # TODO
    raise NotImplementedError


def is_unanswerable(scores: list[float], threshold: float) -> bool:
    """scoreがない、または最大scoreがthreshold未満なら回答不能。"""
    # TODO
    raise NotImplementedError
