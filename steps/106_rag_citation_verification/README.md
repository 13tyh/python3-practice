# 106 RAG Citation Verification

## 学ぶこと

- citationが実在chunkを指すか確認する
- 根拠なし回答を拒否する
- answerable判定を入れる

## 書くこと

- answer内のcitation idを抜く
- citation idの存在を検証する
- 根拠がない回答を失敗扱いにする

## 参考URL

- https://python.langchain.com/docs/concepts/retrieval/

```bash
pytest exercise_tests/rag_citation_verification -q
```
