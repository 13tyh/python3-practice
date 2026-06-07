# 20 File DB Export

目的: DB からデータを取り出し、CSV に変換する処理を読める・書けるようにする。

## 見るポイント

- DB の query 条件
- 取得する field
- `_id` を CSV に出すか
- 日付や `None` の扱い
- CSV の header 順
- encoding
- 大量データ時に全件を memory に載せない工夫

## 実行

```bash
pytest exercise_tests/file_db_export -q
```

## 実務での分け方

- `query.py`: 検索条件を作る
- `transform.py`: DB document を CSV row に変換
- `csv_export.py`: CSV として書く

