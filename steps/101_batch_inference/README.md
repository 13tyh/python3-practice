# 53 Batch Inference

目的: 大量のプロンプトをまとめて推論する「バッチ推論」の考え方を理解する。

## 使いどころ

- 即時レスポンスが不要
- 大量のレビュー、分類、要約を処理したい
- 1件ずつ API を叩くより管理しやすくしたい

## Vertex AI / Gemini

Vertex AI の通常モデルでは `Model.batch_predict` や `BatchPredictionJob` を使う。
Gemini では Vertex AI 上の Batch inference を使い、JSONL や BigQuery などを入力にできる。

## 見るポイント

- 入力と出力の保存先
- model 名
- location
- job 名
- JSONL の1行1リクエスト形式
- 失敗行の扱い
- オンライン推論との違い

## 課題

```bash
pytest steps/101_batch_inference/tests -q
```

`steps/101_batch_inference/implementation/exercises/batch_inference/` の TODO を埋める。


