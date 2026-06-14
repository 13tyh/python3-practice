# 130 FastAPI Middleware Lifespan

## 学ぶこと

- middlewareでrequest idやlatencyを記録する
- CORSを環境ごとに制御する
- lifespanで起動時接続と終了時切断を扱う

## 書くこと

- request logを組み立てる
- origin許可を判定する
- resourceの接続/切断順を作る

## 参考URL

- https://fastapi.tiangolo.com/tutorial/middleware/
- https://fastapi.tiangolo.com/advanced/events/

```bash
pytest steps/130_fastapi_middleware_lifespan/tests -q
```

