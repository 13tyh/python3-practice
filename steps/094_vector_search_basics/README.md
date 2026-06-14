# 68 Vector Search Basics

## 学ぶこと

- embeddingを数値ベクトルとして読む
- cosine similarityを自力で計算する
- RAGのretrieverが何をしているか理解する

## 書くこと

- cosine similarityを実装する
- queryに近いdocumentをtop-kで返す
- score順を安定させる

## 注意点

- 次元数が違うvectorを比較しない
- scoreが高いことと正しい回答は別
- retrieval結果にはidとscoreを残す

## 参考URL

- https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity

```bash
pytest steps/094_vector_search_basics/tests -q
```

