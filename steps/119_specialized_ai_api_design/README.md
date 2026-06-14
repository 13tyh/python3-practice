# 119 Specialized AI API Design

## 学ぶこと

- 特化型AIのAPIは入力、context、answer、citation、decisionを分ける
- model出力をそのまま返さない
- user向けレスポンスと監査用情報を分ける

## 書くこと

- requestを検証する
- response skeletonを作る
- answerable/blockedの状態を返す

## 参考URL

- https://fastapi.tiangolo.com/tutorial/response-model/

```bash
pytest steps/119_specialized_ai_api_design/tests -q
```

