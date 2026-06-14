# 27 Processes

目的: `subprocess` と `multiprocessing` を読める・書ける・危険性を判断できるようにする。

## subprocess

外部コマンドを Python から実行する仕組み。

見るポイント:

- `shell=True` を安易に使わない
- コマンドは文字列ではなく `list[str]` で渡す
- `returncode`, `stdout`, `stderr` を見る
- `timeout` を付ける
- 失敗時に握りつぶさない

例:

```python
subprocess.run(["python", "--version"], capture_output=True, text=True, timeout=5)
```

## multiprocessing

CPU を使う重い処理を複数プロセスに分ける仕組み。

見るポイント:

- I/O 待ちは `asyncio` や thread の方が合うこともある
- Windows では `if __name__ == "__main__":` が重要
- プロセス間で共有する値はコピーされる
- 大きいデータを渡すと逆に遅くなる
- 例外、終了、タイムアウトを考える

## 課題

```bash
pytest steps/060_processes/tests -q
```

`steps/060_processes/implementation/exercises/processes/` の TODO を埋める。


