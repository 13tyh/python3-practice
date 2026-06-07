# Debugging

エラーを読めるようにする練習。

## traceback の読み方

1. 一番下の例外名を見る
2. 自分のファイルの行を探す
3. 期待した値と実際の値を比べる
4. 最小入力で再現する

## breakpoint

```python
breakpoint()
```

コンテナ内で pytest を止めて変数を見る。

```bash
pytest path/to/test.py -q -s
```

## ログで追う

- request id
- user id
- action
- status
- elapsed time

