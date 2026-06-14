# 109 AI Observability Traces

## 学ぶこと

- request_id、model、prompt_version、latencyを記録する
- AI呼び出しの調査に必要な文脈を残す
- token/costをログへ出す

## 書くこと

- trace eventを作る
- latency bucketを返す
- secretを含まないログcontextを作る

## 参考URL

- https://opentelemetry.io/docs/languages/python/

```bash
pytest steps/109_ai_observability_traces/tests -q
```

