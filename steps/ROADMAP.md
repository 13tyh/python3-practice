# Roadmap

## Phase 1: Python 基礎集中

- `001_syntax`、`002_boolean_logic` から `013_custom_exceptions`
- `014_collections_deep` から `022_error_design_deep`
- `023_typing_deep`、`024_static_typing_practice`、`025_files`、`026_datetime_timezone`
- bool、文字列、list、dict、set、関数、型、ファイル、日時を序盤で固める
- collections、itertools、dataclass、context manager、typing追加、import、regex、探索、例外設計を反復する

## Phase 2: テスト、ログ、設計

- `027_testing_deep`、`028_mocking_external_services`、`029_property_based_thinking`
- `030_core_design_thinking` から `040_advanced`
- `033_debugging_deep`、`037_domain_modeling`、`041_architecture_decision_records`
- テスト、logger、traceback、責務分割、設計判断を扱える

## Phase 3: FastAPI と外部API

- `042_pydantic_validation` から `060_processes`
- `061_fastapi_middleware_lifespan` から `063_auth_jwt_rbac`
- `046_settings_secrets`、`049_webhooks_events`、`051_api_pagination_deep`
- `052_rate_limiting`、`053_openapi_contract`、`056_resilience_patterns`
- FastAPI、認証、例外、API設計、外部API、async、processを読める
- middleware、lifespan、file upload、WebSocket、JWT/RBACを扱える

## Phase 4: DB、性能、データ処理

- `064_performance` から `085_log_analysis`
- `065_memory_profiling`、`072_schema_evolution`、`076_background_tasks`
- `077_scheduler_cron`、`078_etl_pipeline`、`080_streaming_files_large`、`083_data_contracts`
- `086_mongo_ops_schema`、`087_worker_dead_letter`、`088_data_analysis_stats`
- N+1、index、transaction、cache、job、CSV/PDF/分析を扱える
- slow query、schema validation、dead letter、外れ値検出を扱える

## Phase 5: AI/RAG

- `089_model_mapping` から `103_ai_agents`
- `090_ai_cost_control`、`094_vector_search_basics`、`104_prompt_templates` から `126_domain_ai_release_checklist`
- `127_ai_dataset_versioning`、`128_ai_ab_drift`、`129_rag_ops_quality`
- deployment_name、model_name、token budget、LangChain、LangGraph、RAGを説明できる
- prompt、structured output、tool calling、memory、safety、fallback、AI観測を扱える
- 特化型AIの要件、専門知識、評価、feedback、guardrails、release判定を扱える
- dataset versioning、A/B test、drift、RAG運用品質を扱える

## Phase 6: 統合とレビュー

- `130_fastapi_ai`、`131_ai_review`、`132_review_comments`、`133_api_compatibility_design`、`134_capstone`
- FastAPI + AI service を統合し、AI出力をレビューできる
- API互換性と破壊的変更を判断できる

## Phase 7: 運用・開発フロー

- `135_cli_tools`、`136_ci_debugging`、`137_docker_ops`、`138_git_workflow`、`139_feature_flags`
- `140_security_scanning`、`141_observability_slo`、`142_deploy_release_strategy`
- CLI、CI、Docker、Git、feature flagを現場目線で扱える
- security scan、SLO、canary、blue/green、rollbackを扱える
