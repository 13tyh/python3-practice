# 102 Conversation Memory

## 学ぶこと

- 会話履歴を無制限に渡さない
- token budgetに合わせて古い履歴を削る
- system messageを保持する

## 書くこと

- messageを末尾優先でtrimする
- roleごとにmessageを数える
- memory summaryを作る

## 参考URL

- https://docs.langchain.com/oss/python/langchain/short-term-memory

```bash
pytest steps/108_conversation_memory/tests -q
```

