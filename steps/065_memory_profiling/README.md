# 82 Memory Profiling

## 学ぶこと

- メモリ上限からchunk sizeを考える
- 一括読み込みを避ける
- O(n)でもメモリで落ちるケースを想像する

## 書くこと

- listをchunkへ分ける
- 1行サイズと上限から件数を見積もる
- 0や負数を拒否する

## 参考URL

- https://docs.python.org/3/library/tracemalloc.html

```bash
pytest steps/065_memory_profiling/tests -q
```

