# 59 CLI Tools

## 学ぶこと

- `argparse` でコマンドライン引数を受け取る
- `--limit` や `--dry-run` のような実務でよく見るoptionを読む
- CLIの入力を内部処理用のdictへ変換する

## 書くこと

- parserを作る
- argvからNamespaceを作る
- 実行設定をsummaryとして返す

## 注意点

- CLI引数を文字列のまま業務ロジックへ流さない
- default値をREADMEやhelpと一致させる
- `argparse` の例外を握りつぶさない

## 参考URL

- https://docs.python.org/3/library/argparse.html

```bash
pytest steps/135_cli_tools/tests -q
```

