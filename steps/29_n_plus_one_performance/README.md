# 56 N Plus One Performance

目的: N+1 問題や無駄なループを見つけ、まとめて取得・変換する書き方を身につける。

## N+1 とは

一覧を1回取得したあと、各行ごとに追加 query / API call を投げてしまう問題。

悪い例:

```python
orders = repo.list_orders()
for order in orders:
    user = repo.find_user(order.user_id)
```

良い方向:

```python
orders = repo.list_orders()
users = repo.find_users_by_ids([order.user_id for order in orders])
```

## 見るポイント

- loop の中で DB / API を呼んでいないか
- `id -> object` の辞書を作れるか
- query 回数を数えられるか
- 大量データを chunk に分けているか
- list を何度も full scan していないか

## 実行

```bash
pytest exercise_tests/n_plus_one_performance -q
```

