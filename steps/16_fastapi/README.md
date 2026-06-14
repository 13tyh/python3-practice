# 16 FastAPI

目的: FastAPI の基本と、`schema/router/service` の分け方を理解する。

## 基本

- `FastAPI()` で app を作る
- `@app.get`, `@router.post` で endpoint を作る
- Request / Response は Pydantic model にする
- 業務ロジックは router に書きすぎない

## 実行

```bash
pytest steps/16_fastapi/tests -q
uvicorn exercises.fastapi_app.main:app --host 0.0.0.0 --port 8000 --reload
```

ブラウザで見る:

```text
http://localhost:8000/docs
```


