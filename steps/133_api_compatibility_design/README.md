# 142 API Compatibility Design

## 学ぶこと

- field削除は破壊的変更
- required追加は破壊的変更
- deprecation header

## 書くこと

- 削除fieldを検出する
- required追加を判定する
- 非推奨headerを返す

## 参考URL

- https://spec.openapis.org/oas/latest.html

```bash
pytest steps/133_api_compatibility_design/tests -q
```

