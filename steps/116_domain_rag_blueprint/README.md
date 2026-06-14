# 116 Domain RAG Blueprint

## 学ぶこと

- 特化型AIではRAG設計が業務知識の入口になる
- 文書種別ごとにchunk戦略を変える
- retrieval、rerank、citation、拒否条件を設計する

## 書くこと

- 文書種別からchunk sizeを選ぶ
- queryにmetadata filterが必要か判定する
- RAG構成のblueprintを返す

## 参考URL

- https://docs.langchain.com/oss/python/langchain/retrieval

```bash
pytest steps/116_domain_rag_blueprint/tests -q
```

