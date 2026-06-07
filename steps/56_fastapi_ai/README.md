# 56 FastAPI AI

目的: FastAPI の `router/schema/service` 分割で、LangChain などの AI 処理を API 化する。

## 基本方針

- `schema.py`: request / response の型
- `service.py`: prompt 作成、AI 呼び出し、出力整形
- `router.py`: HTTP 入出力だけ担当
- `main.py`: app と依存を組み立てる

## 判断ポイント

- router に prompt を直書きしていないか
- API key を router や schema に持ち込んでいないか
- LLM を fake に差し替えてテストできるか
- AI の返答をそのまま返さず、response schema に整えているか

## 実行

```bash
pytest exercise_tests/fastapi_ai_app -q
uvicorn exercises.fastapi_ai_app.main:app --host 0.0.0.0 --port 8000 --reload
```

