# 58 Capstone

実務風の最終課題。

## 作るもの

学習ログ API の内部ロジック。

要件:

- 学習記録を MongoDB に保存する
- topic、minutes、memo、created_at を持つ
- topic ごとの合計時間を集計する
- LangChain で memo の改善提案を作る
- LangGraph で次の学習アクションを決める
- pytest で主要ロジックを守る

## 完了条件

- `pytest -q` が通る
- `ruff check .` が通る
- `mypy src` が通る
- README に設計判断を書ける
- AI 出力の採用理由と不採用理由を書ける


