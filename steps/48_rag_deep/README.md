# 48 RAG Deep

目的: RAG を「なんとなく検索」ではなく、分割・検索・評価・回答生成の流れで理解する。

## 流れ

1. document を読む
2. chunk に分割する
3. chunk に metadata を付ける
4. query で検索する
5. context を作る
6. LLM に渡す
7. 検索結果と回答を評価する

## 見るポイント

- chunk size
- overlap
- metadata
- top_k
- score threshold
- 引用元
- 回答できない時の扱い

## 実行

```bash
pytest steps/48_rag_deep/tests -q
```


