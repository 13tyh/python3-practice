# 60 Static Typing Practice

## 学ぶこと

- `TypedDict` で外部入力の形を読む
- `int | str | None` のようなunion型を安全に絞り込む
- 型ヒントが嘘になりやすい箇所を見抜く

## 書くこと

- 文字列の年齢をintへ変換する
- 不正な入力を `None` として扱う
- 正規化済みのuser dictを返す

## 注意点

- `dict[str, Any]` に逃げるとレビューしにくくなる
- `None` をintとして扱わない
- 型変換の失敗条件をテストで固定する

## 参考URL

- https://docs.python.org/3/library/typing.html
- https://mypy.readthedocs.io/en/stable/type_narrowing.html

```bash
pytest exercise_tests/static_typing -q
```
