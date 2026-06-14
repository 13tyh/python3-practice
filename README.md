# Python Master

Docker コンテナ内で Python 3 を学び、既存プロジェクトに参画した時に「読める・書ける・直せる・判断できる・提案できる」状態を目指す学習環境です。

## 完成状態

このリポジトリは、Docker だけで Python 学習環境、MongoDB、実行API、Vue/TypeScript の学習UIまで起動できる状態です。

- ローカルに Python / Node.js / npm / pnpm がなくても起動可能
- 初期表示は `http://localhost:5173/#home`
- Stepごとに「問題」「学ぶこと」「書くファイル」「参照リソース」「実行コマンド」を確認可能
- Step画面は `読む / 書く / 実行 / 振り返り` の順に整理
- ホームに `今日やる3問`、翌日復習、基礎ランダム候補を表示
- UI上の `実行` から許可済みコマンドを実行可能
- Stepの完了チェックは、対象テストが成功した時だけ付く
- ホームで効率ルート、苦手カテゴリ、今日やるStepを確認可能
- RAG可視化、MongoDB練習、レビュー課題、解答例比較をAPIキーなしで利用可能
- APIキー不要の疑似AI実験で、AI出力採点、FastAPI責務分割、RAG chunk比較を練習可能
- GitHub Actions で Docker build、Python品質チェック、frontend test/e2e/build を確認

## 起動

Windows PowerShell / macOS Terminal 共通です。

```bash
docker compose up -d --build
```

ブラウザで次を開きます。

- 学習UI: `http://localhost:5173/#home`
- 実行API: `http://localhost:8000`

コンテナに入って直接操作する場合:

```bash
docker compose exec app bash
```

Vue と実行APIは hot reload 対応です。`frontend/`、`tools/`、`docs/` の変更は保存後に反映されます。

Docker Desktop では次の固定名で表示されます。

- `python-master-frontend`: Vue/TypeScript 学習UI
- `python-master-api`: UI実行用API
- `python-master-app`: Python学習用コンテナ
- `python-master-mongo`: 練習用MongoDB
- `python-master-mongo-express`: MongoDB確認UI

## 画面でできること

### Home dashboard

![Home dashboard](docs/assets/home-dashboard.png)

### Step workflow

![Step workflow](docs/assets/step-workflow.png)

- ホーム: 効率ルート、苦手カテゴリ、今日の候補、学習状況を見る
- Step画面: 読む、書く、実行、振り返りをタブで切り替える
- 実行: UIから `pytest` / `uv run ...` など許可済みコマンドを実行する
- 比較: 解答例ファイルがあるStepだけ `solutions/` と見比べる
- 実務ラボ: レビュー練習、AI出力採点、RAG可視化、Mongoコマンド確認、メモを使う
- 絞り込み: 今日、未完了、基礎復習、軽量モードで学習量を調整する
- リセット: 進捗と学習ログを最初からやり直す

ショートカット:

- `j`: 次のStep
- `k`: 前のStep
- `r`: 現在Stepの主コマンドを実行
- `/`: Step検索を開く
- `s`: サイドバー開閉
- `l`: 軽量モード切り替え
- `h`: ホームへ戻る
- `Esc`: モーダルを閉じる

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

MongoDBをブラウザで見たい時だけ、tools profileを使います。

```bash
docker compose --profile tools up -d mongo-express
```

`http://localhost:8081` を開きます。

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
uv run lint
uv run fmt
uv run fmt --fix
uv run build
```

基本は Docker 内で作業すれば、Windows/Mac の差をほぼ気にせず進められます。

## Docker ビルド高速化

BuildKit を有効にすると、`uv` と `pnpm` の依存キャッシュが再利用されます。

PowerShell:

```powershell
$env:DOCKER_BUILDKIT=1
$env:COMPOSE_DOCKER_CLI_BUILD=1
docker compose build app frontend
```

macOS / Linux:

```bash
DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker compose build app frontend
```

## CI / リリース確認

GitHub Actions は `.github/workflows/ci.yml` で次を実行します。

- `docker compose build app frontend`
- `docker compose run --rm --no-deps app uv run build`
- `docker compose run --rm --no-deps frontend pnpm test`
- `docker compose run --rm --no-deps frontend pnpm test:e2e`
- `docker compose run --rm --no-deps frontend pnpm build`

ローカルで同じ確認をするなら:

```bash
docker compose run --rm --no-deps app uv run build
docker compose run --rm --no-deps frontend pnpm test
docker compose run --rm --no-deps frontend pnpm test:e2e
docker compose run --rm --no-deps frontend pnpm build
```

## トラブルシュート

- 画面が開かない: `docker compose ps` で `frontend` と `api` が起動しているか確認
- UI実行が失敗する: `docker compose logs -f api` でAPIログを確認
- Mongo初期データがない: `docker compose exec mongo mongosh /docker-entrypoint-initdb.d/01_seed.js`
- 依存が壊れた: `docker compose down` 後に `docker compose up -d --build`
- 進捗をやり直す: 画面上部の `リセット` を使う

## 進め方

1. `steps/000_environment` から順番に README を読む
2. `steps/<step_id>/implementation/` の対象コードを書く
3. `pytest -q` で正しいか確認する
4. `ruff check .`、`black --check .`、`mypy src` で品質を確認する
5. AI に出力させたコードは `steps/131_ai_review` の観点でレビューする

どのディレクトリを触るか迷ったら `docs/DIRECTORY_GUIDE.md` を見ます。
基本は `steps/<step_id>/README.md` を読み、`implementation/` を書き、`tests/` で確認します。

## uv

依存関係は `pyproject.toml` に書きます。

```bash
uv --version
uv sync --dev
uv run pytest -q
uv run lint
uv run fmt
uv run fmt --fix
uv run build
```

コマンドの意味:

- `uv run lint`: `ruff check .` と `mypy src`
- `uv run fmt`: フォーマット確認
- `uv run fmt --fix`: 自動修正
- `uv run build`: `fmt`、`lint`、`pytest -q`

## Python 基礎をたくさん書く

まずは `steps/001_syntax/implementation/exercises/basics/01_values.py` から順番に TODO を埋めます。

```bash
pytest exercise_tests -q
```

最初は大量に失敗します。1ファイルずつ直すなら次のように実行します。

```bash
pytest steps/001_syntax/tests/exercise_tests/basics/test_01_values.py -q
```

基礎チェック表は `notes/python_basics_checklist.md` です。

反復練習は `steps/001_syntax/implementation/exercises/basics_repetition/` です。

```bash
pytest steps/001_syntax/tests/exercise_tests/basics_repetition/test_round_01.py -q
pytest steps/001_syntax/tests/exercise_tests/basics_repetition/test_round_02.py -q
pytest steps/001_syntax/tests/exercise_tests/basics_repetition/test_round_03.py -q
pytest steps/001_syntax/tests/exercise_tests/basics_repetition/test_round_04.py -q
pytest steps/001_syntax/tests/exercise_tests/basics_repetition/test_round_05.py -q
```

反復は `round_01` から `round_55` まであります。まとめて実行:

```bash
pytest steps/001_syntax/tests/exercise_tests/basics_repetition -q
```

## 濃い読み物

- `docs/CURRICULUM.md`: 全体の学習設計
- `docs/FASTAPI_AI_ARCHITECTURE.md`: FastAPI で AI API を作る設計
- `docs/REVIEW_CHECKLIST.md`: コードレビュー観点
- `docs/STEP_REFERENCES.md`: 各 step の理解コメントと参考URL
- `docs/DIRECTORY_GUIDE.md`: Stepごとのディレクトリの見方
- `docs/BASICS_REPETITION_PLAN.md`: 基礎反復の進め方
- `docs/mongosh/COMMANDS.md`: mongosh コマンド集
- `docs/mongosh/PRACTICE.md`: mongosh 練習メニュー

## マスター用追加教材

- `steps/<step_id>/solutions/`: 解答例。実ファイルがあるStepだけ置く
- `failure_patterns/`: 失敗パターン集
- `review_tasks/`: 汚いコードのレビュー課題
- `write_tests/`: 自分でテストを書く課題
- `debugging/`: traceback、breakpoint、ログ調査
- `design_memos/`: 設計判断メモ
- `steps/134_capstone/implementation/projects/ai_review_api/`: FastAPI + MongoDB + AI の実務ミニプロジェクト

## Step 一覧

番号順に進めます。

- `000_environment`: Docker、pytest、ruff、mypy の使い方
- `001_syntax`: 基本文法、関数、例外、型ヒント
- `023_typing_deep`: Python の型ヒント、TypedDict、Protocol、Generic
- `025_files`: ファイル操作、JSON、CSV、パス操作
- `026_datetime_timezone`: UTC、JST、aware / naive datetime
- `027_testing_deep`: fixture、fake client、parametrize 発想
- `030_core_design_thinking`: 冪等性、境界値、不変条件、状態遷移、fail fast
- `031_logging`: logger、ログレベル、秘匿情報マスク、例外ログ
- `032_observability`: request id、structured logging、metrics
- `034_project_reading`: 既存コードを読んでバグ修正
- `035_refactoring`: 関数分割、重複削除、仕様維持
- `036_package_design`: import の向き、public/private API
- `038_app_layers`: model.py、service.py、router.py の責務分け
- `039_design_patterns`: factory、strategy、adapter
- `040_advanced`: 設定、Repository、独自例外、ページング、キャッシュ、リトライ
- `042_pydantic_validation`: validator、enum、nested schema
- `043_fastapi`: FastAPI、schema/router/service、TestClient
- `044_dependency_injection`: Depends、repository / client 差し替え
- `045_auth`: API key、Bearer token、role / permission
- `047_error_handling`: domain error、HTTP error、retry 判断
- `048_security`: prompt injection、path traversal、secret leakage
- `050_api_design`: pagination、sorting、error response、idempotency
- `054_network_api`: HTTP、API、JSON、ステータスコード
- `055_api_client`: timeout、retry、backoff、rate limit
- `057_async`: asyncio、gather、timeout
- `058_async_fastapi`: async def、gather、stream の基礎
- `059_concurrency_practice`: semaphore、concurrent API calls、cancel
- `060_processes`: subprocess、multiprocessing、外部プロセス操作
- `064_performance`: generator、chunk処理、計測
- `066_n_plus_one_performance`: N+1 問題、bulk取得、chunk処理、query数
- `067_sql`: SQLite CRUD
- `068_mongo`: MongoDB と mongosh、Python からの DB 操作
- `069_mongosh_commands`: mongosh コマンド集、検索、更新、集計、index、explain
- `070_mongo_aggregation`: MongoDB aggregation pipeline
- `071_mongo_deep`: index、compound index、upsert、explain
- `073_transactions`: transaction、rollback、整合性
- `074_cache`: TTL cache、cache key
- `075_job_queue`: queue、job status、retry
- `079_file_db_export`: DB からデータを取り出して CSV 化
- `081_docs_pdf`: docs を分割して PDF 化
- `082_data_analysis`: クリーニング、欠損、重複、集計
- `084_pandas_excel`: pandas、CSV、Excel 出力
- `085_log_analysis`: JSONL ログ分析、エラー率、処理時間
- `089_model_mapping`: deployment_name から model_name への対応管理
- `091_google_ai`: Gemini API、Vertex AI、Gen AI SDK
- `092_langchain`: LangChain の基本構造
- `093_langgraph`: LangGraph の状態遷移
- `095_rag_basics`: 文書分割、簡易類似検索、RAG 基礎
- `096_rag_deep`: chunk、retriever、context、RAG 評価
- `097_rag_advanced`: hybrid search、metadata filtering、rerank
- `098_rag_practice`: answerable、citation、rerank、chunk size 比較
- `099_llm_ops`: prompt versioning、fallback、guardrails、cost
- `100_ai_streaming`: token streaming、SSE
- `101_batch_inference`: JSONL、Vertex AI / Gemini バッチ推論の設定
- `102_ai_evaluation`: AI 出力評価、正解率、prompt 比較
- `103_ai_agents`: tool calling、planner、memory、human review
- `130_fastapi_ai`: FastAPI で AI service を API 化
- `131_ai_review`: AI 出力を疑い、テストと観点で判断する
- `134_capstone`: 小さな実務風プロジェクト
- `135_cli_tools`: argparse、CLI引数、dry-run
- `024_static_typing_practice`: TypedDict、union型、型の絞り込み
- `037_domain_modeling`: dataclass、自治体subscription、業務ルール
- `051_api_pagination_deep`: cursor pagination、limit、next_cursor
- `078_etl_pipeline`: stream処理、extract/transform/load
- `056_resilience_patterns`: retry、backoff、失敗分類
- `049_webhooks_events`: HMAC署名、event冪等性
- `136_ci_debugging`: GitHub Actionsログ、pytest失敗行
- `137_docker_ops`: healthcheck、env、degraded状態
- `094_vector_search_basics`: cosine similarity、top-k検索
- `090_ai_cost_control`: token budget、model limit、model選択
- `072_schema_evolution`: backfill、migration、schema互換性
- `138_git_workflow`: git status、ahead/behind、差分確認
- `132_review_comments`: severity、問題、修正案
- `139_feature_flags`: rollout、段階リリース、緊急停止
- `046_settings_secrets`: 必須設定、secret mask、公開設定
- `052_rate_limiting`: fixed window、429、retry after
- `076_background_tasks`: job状態、idempotency key
- `077_scheduler_cron`: due判定、定期実行、再実行安全性
- `083_data_contracts`: required fields、schema version、互換性
- `053_openapi_contract`: OpenAPI、method/path/status
- `028_mocking_external_services`: fake client、呼び出し履歴
- `029_property_based_thinking`: 冪等性、正規化、不変条件
- `065_memory_profiling`: chunk size、メモリ上限
- `080_streaming_files_large`: 巨大ファイル、line stream
- `033_debugging_deep`: traceback、例外名、file/line
- `041_architecture_decision_records`: ADR、設計判断メモ
- `002_boolean_logic`: bool条件、truthy/falsy
- `003_string_formatting_parsing`: f-string、split、strip、join
- `007_sequence_unpacking`: tuple unpacking、*rest
- `008_function_arguments`: default、keyword-only、option
- `009_scope_modules`: scope、module定数、public関数
- `004_list_methods`: append、extend、非破壊更新
- `005_dict_methods`: get、count、merge
- `006_set_operations`: unique、intersection、difference
- `010_comprehension_deep`: list/dict/set内包表記
- `011_iterable_generator_basics`: iterable、generator、yield
- `012_pathlib_glob`: Path、suffix、ファイル名
- `013_custom_exceptions`: 独自例外、validation
- `104_prompt_templates`: prompt template、必須変数、message分割
- `105_prompt_injection_defense`: prompt injection検出、untrusted context
- `106_structured_output_parsing`: AI JSON出力、required fields
- `107_tool_calling_contracts`: tool allowlist、arguments検証
- `108_conversation_memory`: 会話履歴trim、system保持
- `109_embedding_chunk_metadata`: chunk id、metadata、source
- `110_vector_db_index_design`: dimension、metric、filter fields
- `111_rag_query_rewriting`: query正規化、synonym、metadata filter
- `112_rag_citation_verification`: citation検証、answerable判定
- `113_ai_safety_filters`: PII mask、unsafe intent
- `114_model_fallback_routing`: task別model、fallback判断
- `115_ai_observability_traces`: request_id、latency、token/cost
- `116_ai_regression_dataset`: 回帰評価dataset、model別正解率
- `117_domain_ai_requirements`: 特化型AIの対象業務、利用者、成功条件、対象外
- `118_domain_knowledge_taxonomy`: 業務知識の分類、用語、ルール、例外
- `119_domain_dataset_curation`: 専門データの収集、重複除去、PII除外、分割
- `120_domain_evaluation_rubric`: 専門家目線の評価軸、重み、合格条件
- `121_expert_feedback_loop`: 専門家レビュー、修正理由、再学習候補
- `122_domain_rag_blueprint`: 特化型RAGのsource、chunk、metadata、citation設計
- `123_finetuning_dataset_prep`: fine-tuning用JSONL、役割、禁則、検証
- `124_domain_guardrails_policy`: 業務特化AIの回答制限、確認質問、拒否条件
- `125_specialized_ai_api_design`: 特化型AI APIのrequest/response、trace、評価情報
- `126_domain_ai_release_checklist`: 評価、ログ、安全性、fallback、監視のリリース判定
- `014_collections_deep`: Counter、defaultdict、deque
- `015_itertools_functools`: groupby、partial、lru_cache
- `016_dataclass_deep`: frozen、default_factory、値オブジェクト
- `017_context_manager_deep`: with、__enter__、__exit__、contextmanager
- `018_typing_extras`: Literal、Final、TypeAlias、NewType、cast
- `019_import_module_deep`: public/private、__all__、循環import
- `020_regex_practical`: validation、extract、replaceの正規表現
- `021_algorithm_complexity`: 探索、重複除去、sort key、計算量
- `022_error_design_deep`: retryable/permanent error、validation、例外分類
- `061_fastapi_middleware_lifespan`: middleware、CORS、lifespan
- `062_fastapi_files_websocket`: file upload、path traversal対策、WebSocket
- `063_auth_jwt_rbac`: Bearer token、JWT claim、RBAC
- `086_mongo_ops_schema`: compound index、schema validation、slow query
- `087_worker_dead_letter`: worker retry、backoff、dead letter queue
- `088_data_analysis_stats`: 平均、中央値、IQR外れ値検出
- `127_ai_dataset_versioning`: dataset fingerprint、annotation、label分布
- `128_ai_ab_drift`: A/B test、conversion率、drift検知
- `129_rag_ops_quality`: reindex、search quality log、回答不能判定
- `140_security_scanning`: secret mask、脆弱性、権限漏れ
- `141_observability_slo`: error rate、burn rate、latency alert
- `142_deploy_release_strategy`: canary、blue/green、rollback
- `133_api_compatibility_design`: field削除、required追加、deprecation
