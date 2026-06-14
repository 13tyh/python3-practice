# 77 Scheduler And Cron

## 学ぶこと

- cron的な定期実行を小さい関数で考える
- due判定を書く
- batch処理の再実行安全性を考える

## 書くこと

- 実行対象jobを抽出する
- daily jobの次回実行日を出す
- disabled jobを除外する

## 参考URL

- https://docs.python.org/3/library/datetime.html

```bash
pytest steps/77_scheduler_cron/tests -q
```

