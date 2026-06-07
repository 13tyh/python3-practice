# Curriculum

この教材の目的は、Python を暗記することではなく、既存プロジェクトで読める・直せる・判断できる状態になること。

## Phase 1: Python 基礎集中

対象:

- `00_environment`
- `01_syntax`
- `86_boolean_logic`
- `87_string_formatting_parsing`
- `91_list_methods`
- `92_dict_methods`
- `93_set_operations`
- `88_sequence_unpacking`
- `89_function_arguments`
- `90_scope_modules`
- `94_comprehension_deep`
- `95_iterable_generator_basics`
- `96_pathlib_glob`
- `97_custom_exceptions`
- `121_collections_deep`
- `122_itertools_functools`
- `123_dataclass_deep`
- `124_context_manager_deep`
- `125_typing_extras`
- `126_import_module_deep`
- `127_regex_practical`
- `128_algorithm_complexity`
- `129_error_design_deep`
- `02_typing_deep`
- `60_static_typing_practice`
- `03_files`
- `04_datetime_timezone`

できるようになること:

- bool、文字列、list、dict、set、unpack、関数引数を手で書ける
- 内包表記、generator、pathlib、独自例外を基礎として使える
- collections、itertools、dataclass、context manager、regex、探索を使える
- import設計、追加typing、エラー分類を読める
- 型を見て入力と出力を説明できる
- ファイル、日時、例外が起きる条件を先に考えられる

## Phase 2: テスト、ログ、設計

対象:

- `05_testing_deep`
- `80_mocking_external_services`
- `81_property_based_thinking`
- `06_core_design_thinking`
- `07_logging`
- `08_observability`
- `84_debugging_deep`
- `09_project_reading`
- `10_refactoring`
- `11_package_design`
- `61_domain_modeling`
- `12_app_layers`
- `13_design_patterns`
- `14_advanced`
- `85_architecture_decision_records`

できるようになること:

- テストから仕様を読む
- logger、traceback、request id で原因を追う
- router / service / model の責務を分ける
- 設計判断をメモとして残せる

## Phase 3: FastAPI と外部API

対象:

- `15_pydantic_validation`
- `16_fastapi`
- `17_dependency_injection`
- `18_auth`
- `74_settings_secrets`
- `19_error_handling`
- `20_security`
- `65_webhooks_events`
- `21_api_design`
- `62_api_pagination_deep`
- `75_rate_limiting`
- `79_openapi_contract`
- `22_network_api`
- `23_api_client`
- `64_resilience_patterns`
- `24_async`
- `25_async_fastapi`
- `26_concurrency_practice`
- `27_processes`
- `130_fastapi_middleware_lifespan`
- `131_fastapi_files_websocket`
- `132_auth_jwt_rbac`

できるようになること:

- FastAPI の endpoint と schema を書ける
- 認証、secret、例外、webhook、rate limitを判断できる
- cursor pagination、OpenAPI、外部API clientを読める
- async、subprocess、multiprocessingの使いどころを判断する
- middleware、lifespan、file upload、WebSocket、JWT/RBACを設計できる

## Phase 4: DB、性能、データ処理

対象:

- `28_performance`
- `82_memory_profiling`
- `29_n_plus_one_performance`
- `30_sql`
- `31_mongo`
- `32_mongosh_commands`
- `33_mongo_aggregation`
- `34_mongo_deep`
- `70_schema_evolution`
- `35_transactions`
- `36_cache`
- `37_job_queue`
- `76_background_tasks`
- `77_scheduler_cron`
- `63_etl_pipeline`
- `38_file_db_export`
- `83_streaming_files_large`
- `39_docs_pdf`
- `40_data_analysis`
- `78_data_contracts`
- `41_pandas_excel`
- `42_log_analysis`
- `133_mongo_ops_schema`
- `134_worker_dead_letter`
- `135_data_analysis_stats`

できるようになること:

- N+1、index、bulk取得、メモリ上限を判断する
- mongoshで自治体、group、subscriptionを確認する
- migration、transaction、cache、job、schedulerを扱う
- DBからCSV、docsからPDF、ログ分析まで扱う
- slow query、schema validation、dead letter、外れ値検出を判断できる

## Phase 5: AI / RAG

対象:

- `43_model_mapping`
- `69_ai_cost_control`
- `44_google_ai`
- `45_langchain`
- `46_langgraph`
- `68_vector_search_basics`
- `47_rag_basics`
- `48_rag_deep`
- `49_rag_advanced`
- `50_rag_practice`
- `51_llm_ops`
- `52_ai_streaming`
- `53_batch_inference`
- `54_ai_evaluation`
- `55_ai_agents`
- `98_prompt_templates`
- `99_prompt_injection_defense`
- `100_structured_output_parsing`
- `101_tool_calling_contracts`
- `102_conversation_memory`
- `103_embedding_chunk_metadata`
- `104_vector_db_index_design`
- `105_rag_query_rewriting`
- `106_rag_citation_verification`
- `107_ai_safety_filters`
- `108_model_fallback_routing`
- `109_ai_observability_traces`
- `110_ai_regression_dataset`
- `111_domain_ai_requirements`
- `112_domain_knowledge_taxonomy`
- `113_domain_dataset_curation`
- `114_domain_evaluation_rubric`
- `115_expert_feedback_loop`
- `116_domain_rag_blueprint`
- `117_finetuning_dataset_prep`
- `118_domain_guardrails_policy`
- `119_specialized_ai_api_design`
- `120_domain_ai_release_checklist`
- `136_ai_dataset_versioning`
- `137_ai_ab_drift`
- `138_rag_ops_quality`

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

- `56_fastapi_ai`
- `57_ai_review`
- `72_review_comments`
- `142_api_compatibility_design`
- `58_capstone`

できるようになること:

- FastAPI から AI service を呼ぶ設計を説明する
- AI が出したコードの仕様差分、境界値、テスト不足を指摘できる
- レビューコメントを具体的に書ける
- API互換性と破壊的変更を判断できる

## Phase 7: 運用・開発フロー

対象:

- `59_cli_tools`
- `66_ci_debugging`
- `67_docker_ops`
- `71_git_workflow`
- `73_feature_flags`
- `139_security_scanning`
- `140_observability_slo`
- `141_deploy_release_strategy`

できるようになること:

- CLI、CI、Docker、Gitを開発フローとして扱える
- feature flagで段階リリースと緊急停止を判断できる
- security scan、SLO、canary、blue/green、rollbackを判断できる
