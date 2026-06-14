# 73 Feature Flags

## 学ぶこと

- 新機能をflagで段階リリースする
- user単位のrolloutを安定させる
- 本番事故時に素早く戻せる設計を考える

## 書くこと

- flag設定を読む
- user_idでrollout判定する
- disabled時は必ずFalseにする

## 参考URL

- https://martinfowler.com/articles/feature-toggles.html

```bash
pytest steps/73_feature_flags/tests -q
```

