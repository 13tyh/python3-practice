# 06 Core Design Thinking

目的: 重要な考え方を、処理を書きながら身につける。

## 学ぶ考え方

- idempotency: 同じ処理を何度実行しても結果が壊れない
- boundary: 境界値を先に考える
- invariant: 常に守るべき条件を決める
- state transition: 状態遷移を制限する
- normalization: 入力を処理前に整える
- fail fast: 壊れた入力を早く止める
- pure function: 副作用を分ける
- separation of concerns: 変換、検証、保存を分ける

## 実行

```bash
pytest steps/030_core_design_thinking/tests -q
```


