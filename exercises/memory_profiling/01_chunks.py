"""メモリを意識したchunk処理の練習。"""


def chunked(values: list[int], size: int) -> list[list[int]]:
    """valuesをsizeごとに分割する。sizeが0以下ならValueError。"""
    # TODO
    raise NotImplementedError


def estimate_rows_per_chunk(memory_limit_mb: int, bytes_per_row: int) -> int:
    """メモリ上限から1chunkあたりの行数を見積もる。"""
    # TODO
    raise NotImplementedError
