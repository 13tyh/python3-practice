# Curriculum

この教材の目的は、Python を暗記することではなく、既存プロジェクトで読める・直せる・判断できる状態になること。

## Phase 1: Python 基礎

対象:

- `00_environment`
- `01_syntax`
- `02_typing_deep`
- `03_files`
- `04_datetime_timezone`

できるようになること:

- 型を見て入力と出力を説明する
- list / dict / string / datetime を手で扱う
- 例外が起きる条件を先に考える
- テスト失敗から原因を読む

## Phase 2: テスト、ログ、設計

対象:

- `05_testing_deep`
- `06_core_design_thinking`
- `07_logging`
- `08_observability`
- `09_project_reading`
- `10_refactoring`
- `11_package_design`
- `12_app_layers`
- `13_design_patterns`
- `14_advanced`

できるようになること:

- テストから仕様を読む
- logger と request id で原因を追う
- router / service / model の責務を分ける
- 変更範囲を小さくする

## Phase 3: FastAPI と外部API

対象:

- `15_pydantic_validation`
- `16_fastapi`
- `17_dependency_injection`
- `18_auth`
- `19_error_handling`
- `20_security`
- `21_api_design`
- `22_network_api`
- `23_api_client`
- `24_async`
- `25_async_fastapi`
- `26_concurrency_practice`
- `27_processes`

できるようになること:

- FastAPI の endpoint を書く
- request / response schema を Pydantic で作る
- 認証、例外、API設計、非同期処理を読む
- subprocess / multiprocessing の使いどころを判断する

## Phase 4: DB、性能、データ処理

対象:

- `28_performance`
- `29_n_plus_one_performance`
- `30_sql`
- `31_mongo`
- `32_mongosh_commands`
- `33_mongo_aggregation`
- `34_mongo_deep`
- `35_transactions`
- `36_cache`
- `37_job_queue`
- `38_file_db_export`
- `39_docs_pdf`
- `40_data_analysis`
- `41_pandas_excel`
- `42_log_analysis`

できるようになること:

- N+1、index、bulk取得を判断する
- mongosh で自治体、group、subscription を確認する
- DBからCSV、docsからPDF、ログ分析まで扱う

## Phase 5: AI / RAG

対象:

- `43_model_mapping`
- `44_google_ai`
- `45_langchain`
- `46_langgraph`
- `47_rag_basics`
- `48_rag_deep`
- `49_rag_advanced`
- `50_rag_practice`
- `51_llm_ops`
- `52_ai_streaming`
- `53_batch_inference`
- `54_ai_evaluation`
- `55_ai_agents`

できるようになること:

- deployment_name と model_name を分ける
- LangChain の chain を service に差し込む
- LangGraph の state と node を読む
- RAG の chunk / retriever / citation / evaluation を分ける
- JSONL を作ってバッチ推論の入力を準備する

## Phase 6: 統合と判断力

対象:

- `56_fastapi_ai`
- `57_ai_review`
- `58_capstone`

できるようになること:

- FastAPI から AI service を呼ぶ設計を説明する
- AI が出したコードの仕様差分を見つける
- セキュリティ、ログ、例外、テスト不足を指摘する
- 修正案だけでなく、設計案を出す
