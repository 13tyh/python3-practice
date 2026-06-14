# 00 Environment

目的: Python をローカルに入れず、Docker 内で実行・テスト・静的解析できるようにする。

## やること

```bash
python --version
pytest -q
ruff check .
mypy src
```

## 判断ポイント

- テストが通るだけでなく、型エラーと lint エラーも見る
- エラー文は上から順に読む
- 直す前に「何が期待値で、実際は何か」を言語化する


