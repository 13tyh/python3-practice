# 134 Worker Dead Letter

## 学ぶこと

- worker jobの状態
- retry上限とbackoff
- dead letter queue

## 書くこと

- 次のretry delayを計算する
- dead letter送りを判定する
- job状態を分類する

## 参考URL

- https://docs.celeryq.dev/en/stable/userguide/tasks.html#retrying

```bash
pytest steps/087_worker_dead_letter/tests -q
```

