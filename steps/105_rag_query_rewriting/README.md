# 105 RAG Query Rewriting

## 学ぶこと

- 検索用queryと回答用promptを分ける
- 表記ゆれを正規化する
- metadata filter候補を抽出する

## 書くこと

- queryを正規化する
- synonymを追加する
- `city:xxx` のようなfilterを抽出する

## 参考URL

- https://docs.langchain.com/oss/python/langchain/retrieval

```bash
pytest steps/105_rag_query_rewriting/tests -q
```

