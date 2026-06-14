# AI Review API

実務ミニプロジェクト。

## 目的

FastAPI + MongoDB + AI + logger + settings + pytest + batch JSONL を1つにまとめる。

## 機能

- `POST /reviews`: コードレビューを作成
- `GET /reviews`: 履歴取得
- `POST /batch/reviews`: バッチ推論用 JSONL 作成
- MongoDB に履歴保存
- AI client は fake から始める

## やること

1. `app/schema.py` を読む
2. `app/service.py` の TODO を埋める
3. `app/repository.py` の TODO を埋める
4. `tests/` を自分で追加する
5. `design_memos/` に設計判断を書く

