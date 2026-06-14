"""RAG query rewritingの練習。"""

SYNONYMS = {"自治体": ["市区町村", "municipality"], "契約": ["subscription"]}


def normalize_query(query: str) -> str:
    """検索用に空白と大小文字を正規化する。"""
    # TODO
    raise NotImplementedError


def expand_query(query: str) -> list[str]:
    """queryに含まれる語のsynonymを追加する。"""
    # TODO
    raise NotImplementedError


def extract_metadata_filter(query: str) -> dict[str, str]:
    """`city:tokyo` のようなfilterを抽出する。"""
    # TODO
    raise NotImplementedError
