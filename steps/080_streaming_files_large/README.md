# 83 Streaming Large Files

## 学ぶこと

- 巨大ファイルをline単位で処理する
- 空行やコメントをskipする
- generatorで後続処理へ流す

## 書くこと

- 有効行だけyieldする
- prefixに一致する行を数える
- 途中で全件list化しない

## 参考URL

- https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

```bash
pytest steps/080_streaming_files_large/tests -q
```

