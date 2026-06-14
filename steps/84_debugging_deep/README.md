# 84 Debugging Deep

## 学ぶこと

- tracebackから例外名と場所を読む
- 原因箇所と表面化箇所を分ける
- ログ、breakpoint、再現条件をつなげる

## 書くこと

- traceback文字列から例外名を抜く
- 最後のfile/lineを取得する
- 調査メモを作る

## 参考URL

- https://docs.python.org/3/library/traceback.html

```bash
pytest steps/84_debugging_deep/tests -q
```

