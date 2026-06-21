# Curriculum

この教材の目的は、Python を暗記することではなく、既存プロジェクトで読める・直せる・判断できる状態になること。

## Phase 1: Python 基礎集中

対象:

- `001_syntax`
- `002_boolean_logic`
- `003_string_formatting_parsing`
- `004_list_methods`
- `005_dict_methods`
- `006_set_operations`
- `007_sequence_unpacking`
- `008_function_arguments`
- `009_scope_modules`
- `010_comprehension_deep`
- `011_iterable_generator_basics`
- `012_pathlib_glob`
- `013_custom_exceptions`
- `014_collections_deep`
- `015_itertools_functools`
- `016_dataclass_deep`
- `017_context_manager_deep`
- `018_typing_extras`
- `019_import_module_deep`
- `020_regex_practical`
- `021_algorithm_complexity`
- `022_error_design_deep`
- `023_typing_deep`
- `024_static_typing_practice`
- `025_files`
- `026_datetime_timezone`

できるようになること:

- bool、文字列、list、dict、set、unpack、関数引数を手で書ける
- 内包表記、generator、pathlib、独自例外を基礎として使える
- collections、itertools、dataclass、context manager、regex、探索を使える
- import設計、追加typing、エラー分類を読める
- 型を見て入力と出力を説明できる
- ファイル、日時、例外が起きる条件を先に考えられる

## Phase 2: テスト、ログ、設計

対象:

- `027_testing_deep`
- `028_mocking_external_services`
- `029_property_based_thinking`
- `030_core_design_thinking`
- `031_logging`
- `032_observability`
- `033_debugging_deep`
- `034_project_reading`
- `035_refactoring`
- `036_package_design`
- `037_domain_modeling`
- `038_app_layers`
- `039_design_patterns`
- `040_advanced`
- `041_architecture_decision_records`

できるようになること:

- テストから仕様を読む
- logger、traceback、request id で原因を追う
- router / service / model の責務を分ける
- 設計判断をメモとして残せる

## Phase 3: FastAPI と外部API

対象:

- `042_pydantic_validation`
- `043_fastapi`
- `044_dependency_injection`
- `045_auth`
- `046_settings_secrets`
- `047_error_handling`
- `048_security`
- `049_webhooks_events`
- `050_api_design`
- `051_api_pagination_deep`
- `052_rate_limiting`
- `053_openapi_contract`
- `054_network_api`
- `055_api_client`
- `056_resilience_patterns`
- `057_async`
- `058_async_fastapi`
- `059_concurrency_practice`
- `060_processes`
- `061_fastapi_middleware_lifespan`
- `062_fastapi_files_websocket`
- `063_auth_jwt_rbac`

できるようになること:

- FastAPI の endpoint と schema を書ける
- 認証、secret、例外、webhook、rate limitを判断できる
- cursor pagination、OpenAPI、外部API clientを読める
- async、subprocess、multiprocessingの使いどころを判断する
- middleware、lifespan、file upload、WebSocket、JWT/RBACを設計できる

## Phase 4: DB、性能、データ処理

対象:

- `064_performance`
- `065_memory_profiling`
- `066_n_plus_one_performance`
- `067_sql`
- `068_mongo`
- `069_mongosh_commands`
- `070_mongo_aggregation`
- `071_mongo_deep`
- `072_schema_evolution`
- `073_transactions`
- `074_cache`
- `075_job_queue`
- `076_background_tasks`
- `077_scheduler_cron`
- `078_etl_pipeline`
- `079_file_db_export`
- `080_streaming_files_large`
- `081_docs_pdf`
- `082_data_analysis`
- `083_data_contracts`
- `084_pandas_excel`
- `085_log_analysis`
- `086_mongo_ops_schema`
- `087_worker_dead_letter`
- `088_data_analysis_stats`

できるようになること:

- N+1、index、bulk取得、メモリ上限を判断する
- mongoshで自治体、group、subscriptionを確認する
- migration、transaction、cache、job、schedulerを扱う
- DBからCSV、docsからPDF、ログ分析まで扱う
- slow query、schema validation、dead letter、外れ値検出を判断できる

## Phase 5: AI / RAG

対象:

- `089_model_mapping`
- `090_ai_cost_control`
- `091_google_ai`
- `092_langchain`
- `093_langgraph`
- `094_vector_search_basics`
- `095_rag_basics`
- `096_rag_deep`
- `097_rag_advanced`
- `098_rag_practice`
- `099_llm_ops`
- `100_ai_streaming`
- `101_batch_inference`
- `102_ai_evaluation`
- `103_ai_agents`
- `104_prompt_templates`
- `105_prompt_injection_defense`
- `106_structured_output_parsing`
- `107_tool_calling_contracts`
- `108_conversation_memory`
- `109_embedding_chunk_metadata`
- `110_vector_db_index_design`
- `111_rag_query_rewriting`
- `112_rag_citation_verification`
- `113_ai_safety_filters`
- `114_model_fallback_routing`
- `115_ai_observability_traces`
- `116_ai_regression_dataset`
- `117_domain_ai_requirements`
- `118_domain_knowledge_taxonomy`
- `119_domain_dataset_curation`
- `120_domain_evaluation_rubric`
- `121_expert_feedback_loop`
- `122_domain_rag_blueprint`
- `123_finetuning_dataset_prep`
- `124_domain_guardrails_policy`
- `125_specialized_ai_api_design`
- `126_domain_ai_release_checklist`
- `127_ai_dataset_versioning`
- `128_ai_ab_drift`
- `129_rag_ops_quality`

できるようになること:

- deployment_name と model_name を分ける
- token budget と model limit を見て判断できる
- LangChain / LangGraph / RAG / batch / evaluation を説明できる
- prompt、structured output、tool calling、memoryを安全に扱える
- RAGのmetadata、query rewrite、citation verificationを設計できる
- AIのfallback、safety、observability、regression評価を判断できる
- 特化型AIの要件、専門データ、評価、専門家feedback、release判定を設計できる
- dataset version、A/B test、drift、RAG運用品質を追跡できる

## Phase 6: 統合とレビュー

対象:

- `130_fastapi_ai`
- `131_ai_review`
- `132_review_comments`
- `133_api_compatibility_design`
- `134_capstone`

できるようになること:

- FastAPI から AI service を呼ぶ設計を説明する
- AI が出したコードの仕様差分、境界値、テスト不足を指摘できる
- レビューコメントを具体的に書ける
- API互換性と破壊的変更を判断できる

## Phase 7: 運用・開発フロー

対象:

- `135_cli_tools`
- `136_ci_debugging`
- `137_docker_ops`
- `138_git_workflow`
- `139_feature_flags`
- `140_security_scanning`
- `141_observability_slo`
- `142_deploy_release_strategy`

できるようになること:

- CLI、CI、Docker、Gitを開発フローとして扱える
- feature flagで段階リリースと緊急停止を判断できる
- security scan、SLO、canary、blue/green、rollbackを判断できる
