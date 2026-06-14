# 43 Model Mapping

目的: `deployment_name` と `model_name` の違いを理解する。

## 用語

- `deployment_name`: Azure OpenAI などで作るデプロイ名。アプリが呼ぶ名前。
- `model_name`: 実体のモデル名。例: `gpt-4.1`, `gpt-4.1-mini`。

## なぜ分けるか

- 本番 API の呼び先を固定したまま、裏のモデルを差し替えたい
- 環境ごとに deployment 名が違う
- ログやコスト分析では実 model_name が必要
- AI 評価では deployment ではなく model の比較が必要

## 実行

```bash
pytest steps/089_model_mapping/tests -q
```


