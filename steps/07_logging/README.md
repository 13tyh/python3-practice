# 07 Logging

目的: `print` ではなく `logging` を使って、実務で追えるログを書けるようにする。

## 見るポイント

- logger 名は `__name__`
- level は `DEBUG`, `INFO`, `WARNING`, `ERROR`
- API key や password をログに出さない
- 例外は `logger.exception` で traceback を残す
- ログに残す値は「調査に必要な最小限」にする

## 課題

```bash
pytest steps/07_logging/tests -q
```

`steps/07_logging/implementation/exercises/logging_python/` の TODO を埋める。


