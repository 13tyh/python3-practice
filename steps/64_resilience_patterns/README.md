# 64 Resilience Patterns

## 学ぶこと

- timeout、retry、backoff、retry budgetを考える
- retryしてよい失敗と、してはいけない失敗を分ける
- 外部API障害時のふるまいを設計する

## 書くこと

- HTTP statusからretry可否を返す
- exponential backoffを計算する
- 失敗種別を分類する

## 注意点

- 400系を無限retryしない
- retry回数に上限を持つ
- backoffの最大値を決める

## 参考URL

- https://cloud.google.com/architecture/framework/reliability/retry-transient-errors

```bash
pytest steps/64_resilience_patterns/tests -q
```

