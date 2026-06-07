# FastAPI AI Architecture

FastAPI で AI 系 API を作る時の基本形。

```text
client
  |
router.py
  |
schema.py  <->  service.py  <->  AI client / LangChain / GenAI
                   |
                logger
                   |
                repository
```

## router.py

役割:

- HTTP method と path を定義する
- request schema を受け取る
- service を呼ぶ
- response schema を返す
- HTTPException に変換する

書きすぎ注意:

- prompt 文字列
- API key
- DB の細かい query
- LangChain chain の組み立て

## schema.py

役割:

- request / response の形を定義する
- 必須項目、文字数、数値範囲を表す
- OpenAPI docs に出る契約を作る

見るポイント:

- API の外に出してよい項目だけ response にあるか
- 内部 model と response schema を混ぜていないか
- `str | None` と必須文字列を区別できているか

## service.py

役割:

- prompt を作る
- AI client を呼ぶ
- 出力を整形する
- 空返答、例外、タイムアウトを扱う
- テストで fake に差し替えられるようにする

見るポイント:

- 外部 API 呼び出しを隠せているか
- return type が schema と合っているか
- prompt がテスト可能な関数になっているか

## errors.py

役割:

- AI timeout
- AI output parse error
- upstream unavailable
- retryable / non-retryable の分類

## usage.py

役割:

- input token
- output token
- model_name
- cost estimate
- ログ用 context

## よくある悪い形

```python
@router.post("/review")
def review(payload):
    api_key = "..."
    prompt = "..."
    response = client.generate(prompt)
    return response
```

問題:

- API key が直書き
- prompt をテストしにくい
- response の形が不安定
- 例外処理がない
- service を差し替えられない
