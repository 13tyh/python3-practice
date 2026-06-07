# 120 Domain AI Release Checklist

## 学ぶこと

- 特化型AIはリリース前に評価、ログ、安全性、fallbackを確認する
- blockerを残したまま本番投入しない
- release後の監視項目も決める

## 書くこと

- checklistの未完了項目を出す
- release可能か判定する
- 監視メトリクスを返す

## 参考URL

- https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning

```bash
pytest exercise_tests/domain_ai_release_checklist -q
```
