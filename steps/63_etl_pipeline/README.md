# 63 ETL Pipeline

## 学ぶこと

- CSVやDB行をstreamとして処理する
- extract、transform、loadを分ける
- 不正行を落としながら集計する

## 書くこと

- 有効な行だけをyieldする
- minutesをintへ変換する
- topicごとに学習時間を集計する

## 注意点

- 大量データを安易にlist化しない
- 欠損や不正値を黙って0にしない
- 変換と出力を同じ関数に詰め込まない

## 参考URL

- https://docs.python.org/3/library/csv.html
- https://docs.python.org/3/howto/functional.html#generators

```bash
pytest exercise_tests/etl_pipeline -q
```
