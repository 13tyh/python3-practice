# Python Master

Docker コンテナ内で Python 3 を学び、既存プロジェクトに参画した時に「読める・書ける・直せる・判断できる・提案できる」状態を目指す学習環境です。

## 起動

Windows PowerShell / macOS Terminal 共通です。

```bash
docker compose up -d --build
docker compose exec app bash
```

Vue/TypeScript の step 画面:

```bash
docker compose up -d --build
```

ブラウザで `http://localhost:5173` を開きます。
ローカルに Node.js / npm / pnpm が無くても Docker 内で起動します。
Vue と実行APIは hot reload 対応です。`frontend/`、`tools/`、`docs/` の変更は保存後に反映されます。
画面の `実行` ボタンから、許可された `pytest` / `poetry run ...` コマンドを実行できます。
実行APIは `http://localhost:8000` で起動します。

コンテナ内で使う基本コマンド:

```bash
python --version
pytest -q
ruff check .
black --check .
mypy src
```

MongoDB に入る:

```bash
docker compose exec mongo mongosh
```

初回起動時は `docker/mongo-init/01_seed.js` が自動実行され、`python_master` DB に練習用データが入ります。
既存の `mongo_data` volume がある場合は自動実行されないため、再投入したい時は次を実行します。

```bash
docker compose exec mongo mongosh /docker-entrypoint-initdb.d/01_seed.js
```

## Windows / Mac 共通コマンド

Docker Desktop を起動してから、プロジェクト直下で同じコマンドを使います。

```bash
docker compose up -d --build
docker compose exec app bash
poetry run lint
poetry run fmt
poetry run fmt --fix
poetry run build
```

基本は Docker 内で作業すれば、Windows/Mac の差をほぼ気にせず進められます。

## 進め方

1. `steps/00_environment` から順番に README を読む
2. `src/mastery/` のコードを書く、または修正する
3. `pytest -q` で正しいか確認する
4. `ruff check .`、`black --check .`、`mypy src` で品質を確認する
5. AI に出力させたコードは `steps/57_ai_review` の観点でレビューする

## Poetry

依存関係は `pyproject.toml` に書きます。

```bash
poetry --version
poetry install
poetry run pytest -q
poetry run lint
poetry run fmt
poetry run fmt --fix
poetry run build
```

コマンドの意味:

- `poetry run lint`: `ruff check .` と `mypy src`
- `poetry run fmt`: フォーマット確認
- `poetry run fmt --fix`: 自動修正
- `poetry run build`: `fmt`、`lint`、`pytest -q`

## Python 基礎をたくさん書く

まずは `exercises/basics/01_values.py` から順番に TODO を埋めます。

```bash
pytest exercise_tests -q
```

最初は大量に失敗します。1ファイルずつ直すなら次のように実行します。

```bash
pytest exercise_tests/basics/test_01_values.py -q
```

基礎チェック表は `notes/python_basics_checklist.md` です。

反復練習は `exercises/basics_repetition/` です。

```bash
pytest exercise_tests/basics_repetition/test_round_01.py -q
pytest exercise_tests/basics_repetition/test_round_02.py -q
pytest exercise_tests/basics_repetition/test_round_03.py -q
pytest exercise_tests/basics_repetition/test_round_04.py -q
pytest exercise_tests/basics_repetition/test_round_05.py -q
```

反復は `round_01` から `round_55` まであります。まとめて実行:

```bash
pytest exercise_tests/basics_repetition -q
```

## 濃い読み物

- `docs/CURRICULUM.md`: 全体の学習設計
- `docs/FASTAPI_AI_ARCHITECTURE.md`: FastAPI で AI API を作る設計
- `docs/REVIEW_CHECKLIST.md`: コードレビュー観点
- `docs/STEP_REFERENCES.md`: 各 step の理解コメントと参考URL
- `docs/BASICS_REPETITION_PLAN.md`: 基礎反復の進め方
- `docs/mongosh/COMMANDS.md`: mongosh コマンド集
- `docs/mongosh/PRACTICE.md`: mongosh 練習メニュー

## マスター用追加教材

- `solutions/`: 解答例
- `failure_patterns/`: 失敗パターン集
- `review_tasks/`: 汚いコードのレビュー課題
- `write_tests/`: 自分でテストを書く課題
- `debugging/`: traceback、breakpoint、ログ調査
- `design_memos/`: 設計判断メモ
- `projects/ai_review_api/`: FastAPI + MongoDB + AI の実務ミニプロジェクト

## Step 一覧

番号順に進めます。

- `00_environment`: Docker、pytest、ruff、mypy の使い方
- `01_syntax`: 基本文法、関数、例外、型ヒント
- `02_typing_deep`: Python の型ヒント、TypedDict、Protocol、Generic
- `03_files`: ファイル操作、JSON、CSV、パス操作
- `04_datetime_timezone`: UTC、JST、aware / naive datetime
- `05_testing_deep`: fixture、fake client、parametrize 発想
- `06_core_design_thinking`: 冪等性、境界値、不変条件、状態遷移、fail fast
- `07_logging`: logger、ログレベル、秘匿情報マスク、例外ログ
- `08_observability`: request id、structured logging、metrics
- `09_project_reading`: 既存コードを読んでバグ修正
- `10_refactoring`: 関数分割、重複削除、仕様維持
- `11_package_design`: import の向き、public/private API
- `12_app_layers`: model.py、service.py、router.py の責務分け
- `13_design_patterns`: factory、strategy、adapter
- `14_advanced`: 設定、Repository、独自例外、ページング、キャッシュ、リトライ
- `15_pydantic_validation`: validator、enum、nested schema
- `16_fastapi`: FastAPI、schema/router/service、TestClient
- `17_dependency_injection`: Depends、repository / client 差し替え
- `18_auth`: API key、Bearer token、role / permission
- `19_error_handling`: domain error、HTTP error、retry 判断
- `20_security`: prompt injection、path traversal、secret leakage
- `21_api_design`: pagination、sorting、error response、idempotency
- `22_network_api`: HTTP、API、JSON、ステータスコード
- `23_api_client`: timeout、retry、backoff、rate limit
- `24_async`: asyncio、gather、timeout
- `25_async_fastapi`: async def、gather、stream の基礎
- `26_concurrency_practice`: semaphore、concurrent API calls、cancel
- `27_processes`: subprocess、multiprocessing、外部プロセス操作
- `28_performance`: generator、chunk処理、計測
- `29_n_plus_one_performance`: N+1 問題、bulk取得、chunk処理、query数
- `30_sql`: SQLite CRUD
- `31_mongo`: MongoDB と mongosh、Python からの DB 操作
- `32_mongosh_commands`: mongosh コマンド集、検索、更新、集計、index、explain
- `33_mongo_aggregation`: MongoDB aggregation pipeline
- `34_mongo_deep`: index、compound index、upsert、explain
- `35_transactions`: transaction、rollback、整合性
- `36_cache`: TTL cache、cache key
- `37_job_queue`: queue、job status、retry
- `38_file_db_export`: DB からデータを取り出して CSV 化
- `39_docs_pdf`: docs を分割して PDF 化
- `40_data_analysis`: クリーニング、欠損、重複、集計
- `41_pandas_excel`: pandas、CSV、Excel 出力
- `42_log_analysis`: JSONL ログ分析、エラー率、処理時間
- `43_model_mapping`: deployment_name から model_name への対応管理
- `44_google_ai`: Gemini API、Vertex AI、Gen AI SDK
- `45_langchain`: LangChain の基本構造
- `46_langgraph`: LangGraph の状態遷移
- `47_rag_basics`: 文書分割、簡易類似検索、RAG 基礎
- `48_rag_deep`: chunk、retriever、context、RAG 評価
- `49_rag_advanced`: hybrid search、metadata filtering、rerank
- `50_rag_practice`: answerable、citation、rerank、chunk size 比較
- `51_llm_ops`: prompt versioning、fallback、guardrails、cost
- `52_ai_streaming`: token streaming、SSE
- `53_batch_inference`: JSONL、Vertex AI / Gemini バッチ推論の設定
- `54_ai_evaluation`: AI 出力評価、正解率、prompt 比較
- `55_ai_agents`: tool calling、planner、memory、human review
- `56_fastapi_ai`: FastAPI で AI service を API 化
- `57_ai_review`: AI 出力を疑い、テストと観点で判断する
- `58_capstone`: 小さな実務風プロジェクト
