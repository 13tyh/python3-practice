# Roadmap

## Phase 1: Python 基礎集中

- `00_environment`、`01_syntax`、`86_boolean_logic` から `97_custom_exceptions`
- `121_collections_deep` から `129_error_design_deep`
- `02_typing_deep`、`60_static_typing_practice`、`03_files`、`04_datetime_timezone`
- bool、文字列、list、dict、set、関数、型、ファイル、日時を序盤で固める
- collections、itertools、dataclass、context manager、typing追加、import、regex、探索、例外設計を反復する

## Phase 2: テスト、ログ、設計

- `05_testing_deep`、`80_mocking_external_services`、`81_property_based_thinking`
- `06_core_design_thinking` から `14_advanced`
- `84_debugging_deep`、`61_domain_modeling`、`85_architecture_decision_records`
- テスト、logger、traceback、責務分割、設計判断を扱える

## Phase 3: FastAPI と外部API

- `15_pydantic_validation` から `27_processes`
- `130_fastapi_middleware_lifespan` から `132_auth_jwt_rbac`
- `74_settings_secrets`、`65_webhooks_events`、`62_api_pagination_deep`
- `75_rate_limiting`、`79_openapi_contract`、`64_resilience_patterns`
- FastAPI、認証、例外、API設計、外部API、async、processを読める
- middleware、lifespan、file upload、WebSocket、JWT/RBACを扱える

## Phase 4: DB、性能、データ処理

- `28_performance` から `42_log_analysis`
- `82_memory_profiling`、`70_schema_evolution`、`76_background_tasks`
- `77_scheduler_cron`、`63_etl_pipeline`、`83_streaming_files_large`、`78_data_contracts`
- `133_mongo_ops_schema`、`134_worker_dead_letter`、`135_data_analysis_stats`
- N+1、index、transaction、cache、job、CSV/PDF/分析を扱える
- slow query、schema validation、dead letter、外れ値検出を扱える

## Phase 5: AI/RAG

- `43_model_mapping` から `55_ai_agents`
- `69_ai_cost_control`、`68_vector_search_basics`、`98_prompt_templates` から `120_domain_ai_release_checklist`
- `136_ai_dataset_versioning`、`137_ai_ab_drift`、`138_rag_ops_quality`
- deployment_name、model_name、token budget、LangChain、LangGraph、RAGを説明できる
- prompt、structured output、tool calling、memory、safety、fallback、AI観測を扱える
- 特化型AIの要件、専門知識、評価、feedback、guardrails、release判定を扱える
- dataset versioning、A/B test、drift、RAG運用品質を扱える

## Phase 6: 統合とレビュー

- `56_fastapi_ai`、`57_ai_review`、`72_review_comments`、`142_api_compatibility_design`、`58_capstone`
- FastAPI + AI service を統合し、AI出力をレビューできる
- API互換性と破壊的変更を判断できる

## Phase 7: 運用・開発フロー

- `59_cli_tools`、`66_ci_debugging`、`67_docker_ops`、`71_git_workflow`、`73_feature_flags`
- `139_security_scanning`、`140_observability_slo`、`141_deploy_release_strategy`
- CLI、CI、Docker、Git、feature flagを現場目線で扱える
- security scan、SLO、canary、blue/green、rollbackを扱える
