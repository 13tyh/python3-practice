# 13 App Layers

目的: 実務でよく見る `model.py`、`service.py`、`router.py` の分け方を理解する。

## 基本の責務

- `model.py`: データの形。`User`, `Order`, `CreateUserRequest` など
- `service.py`: 業務ロジック。計算、検証、DB 操作の流れ
- `router.py`: HTTP など外側との接点。入力を受け、service を呼び、レスポンスを返す

## 判断ポイント

- router に業務ロジックを書きすぎていないか
- service が HTTP の都合を知りすぎていないか
- model が便利関数だらけになっていないか
- テストしやすい場所にロジックがあるか

## 課題

```bash
pytest exercise_tests/app_layers -q
```

`exercises/app_layers/` の TODO を埋める。

