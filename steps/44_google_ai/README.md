# 44 Google AI

目的: Gemini API、Vertex AI、Google Gen AI SDK の違いを理解する。

## 使うライブラリ

- `google-genai`
- `google-cloud-aiplatform`

## ざっくり違い

- Gemini API: API key で始めやすい
- Vertex AI: Google Cloud project、location、認証、権限管理が重要
- Gen AI SDK: Gemini Developer API と Vertex AI の両方に寄せやすい SDK

## 見るポイント

- API key をコードに直書きしない
- model 名を設定で変えられるようにする
- レスポンス本文が空のケースを見る
- 料金、リージョン、権限を確認する
- AI の出力はテスト可能な形に変換する

## 課題

```bash
pytest steps/44_google_ai/tests -q
```

`steps/44_google_ai/implementation/exercises/google_ai/01_genai_config.py` の TODO を埋める。


