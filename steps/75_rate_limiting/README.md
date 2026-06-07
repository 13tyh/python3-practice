# 75 Rate Limiting

## 学ぶこと

- fixed window rate limitを理解する
- APIやAI呼び出しを守る
- 429を返す条件を考える

## 書くこと

- window内のrequest数を数える
- limit以内か判定する
- 次に許可される時刻を返す

## 参考URL

- https://cloud.google.com/architecture/rate-limiting-strategies-techniques

```bash
pytest exercise_tests/rate_limiting -q
```
