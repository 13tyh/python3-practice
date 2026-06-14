export type FileTestCommand = {
  command: string;
  file: string;
  label: string;
};

export const fileTestCommandsByStep: Record<string, FileTestCommand[]> = {
  "001_syntax": [
    { file: "steps/001_syntax/implementation/exercises/basics/01_values.py", label: "01_values.py", command: "pytest steps/001_syntax/tests/exercise_tests/basics/test_01_values.py -q" },
    { file: "steps/001_syntax/implementation/exercises/basics/05_list_dict.py", label: "05_list_dict.py", command: "pytest steps/001_syntax/tests/exercise_tests/basics/test_05_list_dict.py -q" },
    { file: "steps/001_syntax/implementation/exercises/basics/09_comprehension.py", label: "09_comprehension.py", command: "pytest steps/001_syntax/tests/exercise_tests/basics/test_09_comprehension.py -q" },
  ],
  "002_boolean_logic": [
    { file: "steps/002_boolean_logic/implementation/exercises/basic_boolean_logic/01_boolean_logic.py", label: "01_boolean_logic.py", command: "pytest steps/002_boolean_logic/tests/exercise_tests/basic_boolean_logic/test_boolean_logic.py -q" },
  ],
  "003_string_formatting_parsing": [
    { file: "steps/003_string_formatting_parsing/implementation/exercises/basic_string_formatting/01_format_parse.py", label: "01_format_parse.py", command: "pytest steps/003_string_formatting_parsing/tests/exercise_tests/basic_string_formatting/test_format_parse.py -q" },
  ],
  "004_list_methods": [
    { file: "steps/004_list_methods/implementation/exercises/basic_list_methods/01_list_methods.py", label: "01_list_methods.py", command: "pytest steps/004_list_methods/tests/exercise_tests/basic_list_methods/test_list_methods.py -q" },
  ],
  "005_dict_methods": [
    { file: "steps/005_dict_methods/implementation/exercises/basic_dict_methods/01_dict_methods.py", label: "01_dict_methods.py", command: "pytest steps/005_dict_methods/tests/exercise_tests/basic_dict_methods/test_dict_methods.py -q" },
  ],
  "006_set_operations": [
    { file: "steps/006_set_operations/implementation/exercises/basic_set_operations/01_sets.py", label: "01_sets.py", command: "pytest steps/006_set_operations/tests/exercise_tests/basic_set_operations/test_sets.py -q" },
  ],
  "007_sequence_unpacking": [
    { file: "steps/007_sequence_unpacking/implementation/exercises/basic_unpacking/01_unpacking.py", label: "01_unpacking.py", command: "pytest steps/007_sequence_unpacking/tests/exercise_tests/basic_unpacking/test_unpacking.py -q" },
  ],
  "008_function_arguments": [
    { file: "steps/008_function_arguments/implementation/exercises/basic_function_arguments/01_arguments.py", label: "01_arguments.py", command: "pytest steps/008_function_arguments/tests/exercise_tests/basic_function_arguments/test_arguments.py -q" },
  ],
  "009_scope_modules": [
    { file: "steps/009_scope_modules/implementation/exercises/basic_scope_modules/01_scope.py", label: "01_scope.py", command: "pytest steps/009_scope_modules/tests/exercise_tests/basic_scope_modules/test_scope.py -q" },
  ],
  "010_comprehension_deep": [
    { file: "steps/010_comprehension_deep/implementation/exercises/basic_comprehension_deep/01_comprehensions.py", label: "01_comprehensions.py", command: "pytest steps/010_comprehension_deep/tests/exercise_tests/basic_comprehension_deep/test_comprehensions.py -q" },
  ],
  "011_iterable_generator_basics": [
    { file: "steps/011_iterable_generator_basics/implementation/exercises/basic_generators/01_generators.py", label: "01_generators.py", command: "pytest steps/011_iterable_generator_basics/tests/exercise_tests/basic_generators/test_generators.py -q" },
  ],
  "012_pathlib_glob": [
    { file: "steps/012_pathlib_glob/implementation/exercises/basic_pathlib_glob/01_pathlib_glob.py", label: "01_pathlib_glob.py", command: "pytest steps/012_pathlib_glob/tests/exercise_tests/basic_pathlib_glob/test_pathlib_glob.py -q" },
  ],
  "013_custom_exceptions": [
    { file: "steps/013_custom_exceptions/implementation/exercises/basic_custom_exceptions/01_custom_exceptions.py", label: "01_custom_exceptions.py", command: "pytest steps/013_custom_exceptions/tests/exercise_tests/basic_custom_exceptions/test_custom_exceptions.py -q" },
  ],
  "014_collections_deep": [
    { file: "steps/014_collections_deep/implementation/exercises/basic_collections/01_collections.py", label: "01_collections.py", command: "pytest steps/014_collections_deep/tests/exercise_tests/basic_collections/test_collections.py -q" },
  ],
  "015_itertools_functools": [
    { file: "steps/015_itertools_functools/implementation/exercises/basic_itertools_functools/01_iter_tools.py", label: "01_iter_tools.py", command: "pytest steps/015_itertools_functools/tests/exercise_tests/basic_itertools_functools/test_iter_tools.py -q" },
  ],
  "016_dataclass_deep": [
    { file: "steps/016_dataclass_deep/implementation/exercises/basic_dataclass_deep/01_dataclass.py", label: "01_dataclass.py", command: "pytest steps/016_dataclass_deep/tests/exercise_tests/basic_dataclass_deep/test_dataclass.py -q" },
  ],
  "017_context_manager_deep": [
    { file: "steps/017_context_manager_deep/implementation/exercises/basic_context_manager/01_context_manager.py", label: "01_context_manager.py", command: "pytest steps/017_context_manager_deep/tests/exercise_tests/basic_context_manager/test_context_manager.py -q" },
  ],
  "018_typing_extras": [
    { file: "steps/018_typing_extras/implementation/exercises/basic_typing_extras/01_typing_extras.py", label: "01_typing_extras.py", command: "pytest steps/018_typing_extras/tests/exercise_tests/basic_typing_extras/test_typing_extras.py -q" },
  ],
  "019_import_module_deep": [
    { file: "steps/019_import_module_deep/implementation/exercises/basic_import_modules/01_import_rules.py", label: "01_import_rules.py", command: "pytest steps/019_import_module_deep/tests/exercise_tests/basic_import_modules/test_import_rules.py -q" },
  ],
  "020_regex_practical": [
    { file: "steps/020_regex_practical/implementation/exercises/basic_regex_practical/01_regex.py", label: "01_regex.py", command: "pytest steps/020_regex_practical/tests/exercise_tests/basic_regex_practical/test_regex.py -q" },
  ],
  "021_algorithm_complexity": [
    { file: "steps/021_algorithm_complexity/implementation/exercises/basic_algorithms/01_algorithms.py", label: "01_algorithms.py", command: "pytest steps/021_algorithm_complexity/tests/exercise_tests/basic_algorithms/test_algorithms.py -q" },
  ],
  "022_error_design_deep": [
    { file: "steps/022_error_design_deep/implementation/exercises/basic_error_design/01_error_design.py", label: "01_error_design.py", command: "pytest steps/022_error_design_deep/tests/exercise_tests/basic_error_design/test_error_design.py -q" },
  ],
  "023_typing_deep": [
    { file: "steps/023_typing_deep/implementation/exercises/typing_deep/01_type_basics.py", label: "01_type_basics.py", command: "pytest steps/023_typing_deep/tests/exercise_tests/typing_deep/test_01_type_basics.py -q" },
    { file: "steps/023_typing_deep/implementation/exercises/typing_deep/02_protocol_generic.py", label: "02_protocol_generic.py", command: "pytest steps/023_typing_deep/tests/exercise_tests/typing_deep/test_02_protocol_generic.py -q" },
  ],
  "024_static_typing_practice": [
    { file: "steps/024_static_typing_practice/implementation/exercises/static_typing/01_type_narrowing.py", label: "01_type_narrowing.py", command: "pytest steps/024_static_typing_practice/tests/exercise_tests/static_typing/test_type_narrowing.py -q" },
  ],
  "025_files": [
    { file: "steps/025_files/implementation/exercises/basics/08_files.py", label: "08_files.py", command: "pytest steps/025_files/tests/exercise_tests/basics/test_08_files.py -q" },
    { file: "steps/025_files/implementation/exercises/basics/16_json_csv.py", label: "16_json_csv.py", command: "pytest steps/025_files/tests -q" },
    { file: "steps/025_files/implementation/exercises/file_db_export/csv_export.py", label: "csv_export.py", command: "pytest steps/025_files/tests/exercise_tests/file_db_export/test_transform_csv.py -q" },
  ],
  "026_datetime_timezone": [
    { file: "steps/026_datetime_timezone/implementation/exercises/datetime_timezone/01_timezone.py", label: "01_timezone.py", command: "pytest steps/026_datetime_timezone/tests/exercise_tests/datetime_timezone/test_timezone.py -q" },
  ],
  "027_testing_deep": [
    { file: "steps/027_testing_deep/implementation/exercises/testing_deep/01_test_doubles.py", label: "01_test_doubles.py", command: "pytest steps/027_testing_deep/tests/exercise_tests/testing_deep/test_test_doubles.py -q" },
    { file: "steps/027_testing_deep/implementation/exercises/testing_deep/02_monkeypatch_env.py", label: "02_monkeypatch_env.py", command: "pytest steps/027_testing_deep/tests/exercise_tests/testing_deep/test_monkeypatch_env.py -q" },
  ],
  "028_mocking_external_services": [
    { file: "steps/028_mocking_external_services/implementation/exercises/mocking_external_services/01_fake_client.py", label: "01_fake_client.py", command: "pytest steps/028_mocking_external_services/tests/exercise_tests/mocking_external_services/test_fake_client.py -q" },
  ],
  "029_property_based_thinking": [
    { file: "steps/029_property_based_thinking/implementation/exercises/property_thinking/01_invariants.py", label: "01_invariants.py", command: "pytest steps/029_property_based_thinking/tests/exercise_tests/property_thinking/test_invariants.py -q" },
  ],
  "030_core_design_thinking": [
    { file: "steps/030_core_design_thinking/implementation/exercises/core_design_thinking/01_idempotency.py", label: "01_idempotency.py", command: "pytest steps/030_core_design_thinking/tests/exercise_tests/core_design_thinking/test_01_idempotency.py -q" },
    { file: "steps/030_core_design_thinking/implementation/exercises/core_design_thinking/07_pure_side_effect.py", label: "07_pure_side_effect.py", command: "pytest steps/030_core_design_thinking/tests/exercise_tests/core_design_thinking/test_07_pure_side_effect.py -q" },
  ],
  "031_logging": [
    { file: "steps/031_logging/implementation/exercises/logging_python/01_logger_basics.py", label: "01_logger_basics.py", command: "pytest steps/031_logging/tests/exercise_tests/logging_python/test_01_logger_basics.py -q" },
    { file: "steps/031_logging/implementation/exercises/logging_python/02_error_logging.py", label: "02_error_logging.py", command: "pytest steps/031_logging/tests/exercise_tests/logging_python/test_02_error_logging.py -q" },
  ],
  "032_observability": [
    { file: "steps/032_observability/implementation/exercises/observability/01_observability.py", label: "01_observability.py", command: "pytest steps/032_observability/tests/exercise_tests/observability/test_observability.py -q" },
  ],
  "033_debugging_deep": [
    { file: "steps/033_debugging_deep/implementation/exercises/debugging_deep/01_traceback_reader.py", label: "01_traceback_reader.py", command: "pytest steps/033_debugging_deep/tests/exercise_tests/debugging_deep/test_traceback_reader.py -q" },
  ],
  "035_refactoring": [
    { file: "steps/035_refactoring/implementation/exercises/refactoring/01_refactor_targets.py", label: "01_refactor_targets.py", command: "pytest steps/035_refactoring/tests/exercise_tests/refactoring/test_refactor_targets.py -q" },
    { file: "steps/035_refactoring/implementation/exercises/refactoring/02_code_smells.py", label: "02_code_smells.py", command: "pytest steps/035_refactoring/tests/exercise_tests/refactoring/test_code_smells.py -q" },
  ],
  "036_package_design": [
    { file: "steps/036_package_design/implementation/exercises/package_design/01_import_rules.py", label: "01_import_rules.py", command: "pytest steps/036_package_design/tests/exercise_tests/package_design/test_import_rules.py -q" },
  ],
  "037_domain_modeling": [
    { file: "steps/037_domain_modeling/implementation/exercises/domain_modeling/01_domain_model.py", label: "01_domain_model.py", command: "pytest steps/037_domain_modeling/tests/exercise_tests/domain_modeling/test_domain_model.py -q" },
  ],
  "038_app_layers": [
    { file: "steps/038_app_layers/implementation/exercises/app_layers/model.py", label: "model.py", command: "pytest steps/038_app_layers/tests/exercise_tests/app_layers/test_layers.py -q" },
    { file: "steps/038_app_layers/implementation/exercises/app_layers/router.py", label: "router.py", command: "pytest steps/038_app_layers/tests/exercise_tests/app_layers/test_layers.py -q" },
    { file: "steps/038_app_layers/implementation/exercises/app_layers/service.py", label: "service.py", command: "pytest steps/038_app_layers/tests/exercise_tests/app_layers/test_layers.py -q" },
  ],
  "039_design_patterns": [
    { file: "steps/039_design_patterns/implementation/exercises/design_patterns/01_patterns.py", label: "01_patterns.py", command: "pytest steps/039_design_patterns/tests/exercise_tests/design_patterns/test_patterns.py -q" },
  ],
  "040_advanced": [
    { file: "steps/040_advanced/implementation/exercises/advanced/01_config.py", label: "01_config.py", command: "pytest steps/040_advanced/tests/exercise_tests/advanced/test_01_config.py -q" },
    { file: "steps/040_advanced/implementation/exercises/advanced/05_cache_retry.py", label: "05_cache_retry.py", command: "pytest steps/040_advanced/tests/exercise_tests/advanced/test_05_cache_retry.py -q" },
  ],
  "041_architecture_decision_records": [
    { file: "steps/041_architecture_decision_records/implementation/exercises/adrs/01_decision_record.py", label: "01_decision_record.py", command: "pytest steps/041_architecture_decision_records/tests/exercise_tests/adrs/test_decision_record.py -q" },
  ],
  "042_pydantic_validation": [
    { file: "steps/042_pydantic_validation/implementation/exercises/pydantic_validation/01_validation.py", label: "01_validation.py", command: "pytest steps/042_pydantic_validation/tests/exercise_tests/pydantic_validation/test_validation.py -q" },
  ],
  "043_fastapi": [
    { file: "steps/043_fastapi/implementation/exercises/fastapi_app/main.py", label: "main.py", command: "pytest steps/043_fastapi/tests/exercise_tests/fastapi_app/test_fastapi_app.py -q" },
    { file: "steps/043_fastapi/implementation/exercises/fastapi_app/router.py", label: "router.py", command: "pytest steps/043_fastapi/tests -q" },
    { file: "steps/043_fastapi/implementation/exercises/fastapi_app/service.py", label: "service.py", command: "pytest steps/043_fastapi/tests -q" },
  ],
  "044_dependency_injection": [
    { file: "steps/044_dependency_injection/implementation/exercises/dependency_injection/01_di.py", label: "01_di.py", command: "pytest steps/044_dependency_injection/tests/exercise_tests/dependency_injection/test_di.py -q" },
  ],
  "045_auth": [
    { file: "steps/045_auth/implementation/exercises/auth/01_auth_basics.py", label: "01_auth_basics.py", command: "pytest steps/045_auth/tests/exercise_tests/auth/test_auth_basics.py -q" },
  ],
  "046_settings_secrets": [
    { file: "steps/046_settings_secrets/implementation/exercises/settings_secrets/01_settings.py", label: "01_settings.py", command: "pytest steps/046_settings_secrets/tests/exercise_tests/settings_secrets/test_settings.py -q" },
  ],
  "047_error_handling": [
    { file: "steps/047_error_handling/implementation/exercises/error_handling/01_errors.py", label: "01_errors.py", command: "pytest steps/047_error_handling/tests/exercise_tests/error_handling/test_errors.py -q" },
  ],
  "048_security": [
    { file: "steps/048_security/implementation/exercises/security/01_security_checks.py", label: "01_security_checks.py", command: "pytest steps/048_security/tests/exercise_tests/security/test_security_checks.py -q" },
  ],
  "049_webhooks_events": [
    { file: "steps/049_webhooks_events/implementation/exercises/webhooks/01_webhook_security.py", label: "01_webhook_security.py", command: "pytest steps/049_webhooks_events/tests/exercise_tests/webhooks/test_webhook_security.py -q" },
  ],
  "050_api_design": [
    { file: "steps/050_api_design/implementation/exercises/api_design/01_api_contract.py", label: "01_api_contract.py", command: "pytest steps/050_api_design/tests/exercise_tests/api_design/test_api_contract.py -q" },
  ],
  "051_api_pagination_deep": [
    { file: "steps/051_api_pagination_deep/implementation/exercises/api_pagination_deep/01_cursor.py", label: "01_cursor.py", command: "pytest steps/051_api_pagination_deep/tests/exercise_tests/api_pagination_deep/test_cursor.py -q" },
  ],
  "052_rate_limiting": [
    { file: "steps/052_rate_limiting/implementation/exercises/rate_limiting/01_fixed_window.py", label: "01_fixed_window.py", command: "pytest steps/052_rate_limiting/tests/exercise_tests/rate_limiting/test_fixed_window.py -q" },
  ],
  "053_openapi_contract": [
    { file: "steps/053_openapi_contract/implementation/exercises/openapi_contract/01_openapi_reader.py", label: "01_openapi_reader.py", command: "pytest steps/053_openapi_contract/tests/exercise_tests/openapi_contract/test_openapi_reader.py -q" },
  ],
  "054_network_api": [
    { file: "steps/054_network_api/implementation/exercises/network_api/01_http_basics.py", label: "01_http_basics.py", command: "pytest steps/054_network_api/tests/exercise_tests/network_api/test_01_http_basics.py -q" },
  ],
  "055_api_client": [
    { file: "steps/055_api_client/implementation/exercises/api_client/01_client.py", label: "01_client.py", command: "pytest steps/055_api_client/tests/exercise_tests/api_client/test_client.py -q" },
  ],
  "056_resilience_patterns": [
    { file: "steps/056_resilience_patterns/implementation/exercises/resilience/01_retry_policy.py", label: "01_retry_policy.py", command: "pytest steps/056_resilience_patterns/tests/exercise_tests/resilience/test_retry_policy.py -q" },
  ],
  "057_async": [
    { file: "steps/057_async/implementation/exercises/async_python/01_asyncio_basics.py", label: "01_asyncio_basics.py", command: "pytest steps/057_async/tests/exercise_tests/async_python/test_01_asyncio_basics.py -q" },
  ],
  "058_async_fastapi": [
    { file: "steps/058_async_fastapi/implementation/exercises/async_fastapi/01_async_patterns.py", label: "01_async_patterns.py", command: "pytest steps/058_async_fastapi/tests/exercise_tests/async_fastapi/test_async_patterns.py -q" },
  ],
  "059_concurrency_practice": [
    { file: "steps/059_concurrency_practice/implementation/exercises/concurrency_practice/01_async_limit.py", label: "01_async_limit.py", command: "pytest steps/059_concurrency_practice/tests/exercise_tests/concurrency_practice/test_async_limit.py -q" },
  ],
  "060_processes": [
    { file: "steps/060_processes/implementation/exercises/processes/01_subprocess.py", label: "01_subprocess.py", command: "pytest steps/060_processes/tests/exercise_tests/processes/test_01_subprocess.py -q" },
    { file: "steps/060_processes/implementation/exercises/processes/02_multiprocessing.py", label: "02_multiprocessing.py", command: "pytest steps/060_processes/tests/exercise_tests/processes/test_02_multiprocessing.py -q" },
  ],
  "061_fastapi_middleware_lifespan": [
    { file: "steps/061_fastapi_middleware_lifespan/implementation/exercises/fastapi_middleware_lifespan/01_middleware.py", label: "01_middleware.py", command: "pytest steps/061_fastapi_middleware_lifespan/tests/exercise_tests/fastapi_middleware_lifespan/test_middleware.py -q" },
  ],
  "062_fastapi_files_websocket": [
    { file: "steps/062_fastapi_files_websocket/implementation/exercises/fastapi_files_websocket/01_files_websocket.py", label: "01_files_websocket.py", command: "pytest steps/062_fastapi_files_websocket/tests/exercise_tests/fastapi_files_websocket/test_files_websocket.py -q" },
  ],
  "063_auth_jwt_rbac": [
    { file: "steps/063_auth_jwt_rbac/implementation/exercises/auth_jwt_rbac/01_auth.py", label: "01_auth.py", command: "pytest steps/063_auth_jwt_rbac/tests/exercise_tests/auth_jwt_rbac/test_auth.py -q" },
  ],
  "064_performance": [
    { file: "steps/064_performance/implementation/exercises/performance/01_performance.py", label: "01_performance.py", command: "pytest steps/064_performance/tests/exercise_tests/performance/test_performance.py -q" },
  ],
  "065_memory_profiling": [
    { file: "steps/065_memory_profiling/implementation/exercises/memory_profiling/01_chunks.py", label: "01_chunks.py", command: "pytest steps/065_memory_profiling/tests/exercise_tests/memory_profiling/test_chunks.py -q" },
  ],
  "066_n_plus_one_performance": [
    { file: "steps/066_n_plus_one_performance/implementation/exercises/n_plus_one_performance/01_n_plus_one.py", label: "01_n_plus_one.py", command: "pytest steps/066_n_plus_one_performance/tests/exercise_tests/n_plus_one_performance/test_01_n_plus_one.py -q" },
    { file: "steps/066_n_plus_one_performance/implementation/exercises/n_plus_one_performance/03_performance_review.py", label: "03_performance_review.py", command: "pytest steps/066_n_plus_one_performance/tests/exercise_tests/n_plus_one_performance/test_03_performance_review.py -q" },
  ],
  "067_sql": [
    { file: "steps/067_sql/implementation/exercises/sql_basics/01_sqlite.py", label: "01_sqlite.py", command: "pytest steps/067_sql/tests/exercise_tests/sql_basics/test_sqlite.py -q" },
  ],
  "070_mongo_aggregation": [
    { file: "steps/070_mongo_aggregation/implementation/exercises/mongo_aggregation/01_pipeline.py", label: "01_pipeline.py", command: "pytest steps/070_mongo_aggregation/tests/exercise_tests/mongo_aggregation/test_pipeline.py -q" },
  ],
  "071_mongo_deep": [
    { file: "steps/071_mongo_deep/implementation/exercises/mongo_deep/01_indexes.py", label: "01_indexes.py", command: "pytest steps/071_mongo_deep/tests/exercise_tests/mongo_deep/test_indexes.py -q" },
    { file: "steps/071_mongo_deep/implementation/exercises/mongo_deep/02_migration.py", label: "02_migration.py", command: "pytest steps/071_mongo_deep/tests/exercise_tests/mongo_deep/test_migration.py -q" },
  ],
  "072_schema_evolution": [
    { file: "steps/072_schema_evolution/implementation/exercises/schema_evolution/01_migration_plan.py", label: "01_migration_plan.py", command: "pytest steps/072_schema_evolution/tests/exercise_tests/schema_evolution/test_migration_plan.py -q" },
  ],
  "073_transactions": [
    { file: "steps/073_transactions/implementation/exercises/transactions/01_transaction.py", label: "01_transaction.py", command: "pytest steps/073_transactions/tests/exercise_tests/transactions/test_transaction.py -q" },
  ],
  "074_cache": [
    { file: "steps/074_cache/implementation/exercises/cache/01_ttl_cache.py", label: "01_ttl_cache.py", command: "pytest steps/074_cache/tests/exercise_tests/cache/test_ttl_cache.py -q" },
  ],
  "075_job_queue": [
    { file: "steps/075_job_queue/implementation/exercises/job_queue/01_queue.py", label: "01_queue.py", command: "pytest steps/075_job_queue/tests/exercise_tests/job_queue/test_queue.py -q" },
  ],
  "076_background_tasks": [
    { file: "steps/076_background_tasks/implementation/exercises/background_tasks/01_jobs.py", label: "01_jobs.py", command: "pytest steps/076_background_tasks/tests/exercise_tests/background_tasks/test_jobs.py -q" },
  ],
  "077_scheduler_cron": [
    { file: "steps/077_scheduler_cron/implementation/exercises/scheduler_cron/01_scheduler.py", label: "01_scheduler.py", command: "pytest steps/077_scheduler_cron/tests/exercise_tests/scheduler_cron/test_scheduler.py -q" },
  ],
  "078_etl_pipeline": [
    { file: "steps/078_etl_pipeline/implementation/exercises/etl_pipeline/01_streaming_csv.py", label: "01_streaming_csv.py", command: "pytest steps/078_etl_pipeline/tests/exercise_tests/etl_pipeline/test_streaming_csv.py -q" },
  ],
  "079_file_db_export": [
    { file: "steps/079_file_db_export/implementation/exercises/file_db_export/csv_export.py", label: "csv_export.py", command: "pytest steps/079_file_db_export/tests/exercise_tests/file_db_export/test_transform_csv.py -q" },
    { file: "steps/079_file_db_export/implementation/exercises/file_db_export/query.py", label: "query.py", command: "pytest steps/079_file_db_export/tests/exercise_tests/file_db_export/test_query.py -q" },
    { file: "steps/079_file_db_export/implementation/exercises/file_db_export/transform.py", label: "transform.py", command: "pytest steps/079_file_db_export/tests/exercise_tests/file_db_export/test_transform_csv.py -q" },
  ],
  "080_streaming_files_large": [
    { file: "steps/080_streaming_files_large/implementation/exercises/streaming_files_large/01_lines.py", label: "01_lines.py", command: "pytest steps/080_streaming_files_large/tests/exercise_tests/streaming_files_large/test_lines.py -q" },
  ],
  "081_docs_pdf": [
    { file: "steps/081_docs_pdf/implementation/exercises/docs_pdf/pdf_export.py", label: "pdf_export.py", command: "pytest steps/081_docs_pdf/tests/exercise_tests/docs_pdf/test_pdf_export.py -q" },
    { file: "steps/081_docs_pdf/implementation/exercises/docs_pdf/split_docs.py", label: "split_docs.py", command: "pytest steps/081_docs_pdf/tests/exercise_tests/docs_pdf/test_pdf_export.py steps/081_docs_pdf/tests/exercise_tests/docs_pdf/test_split_docs.py -q" },
  ],
  "082_data_analysis": [
    { file: "steps/082_data_analysis/implementation/exercises/data_analysis/01_cleaning.py", label: "01_cleaning.py", command: "pytest steps/082_data_analysis/tests/exercise_tests/data_analysis/test_cleaning.py -q" },
    { file: "steps/082_data_analysis/implementation/exercises/data_analysis/02_aggregation.py", label: "02_aggregation.py", command: "pytest steps/082_data_analysis/tests/exercise_tests/data_analysis/test_aggregation.py -q" },
  ],
  "083_data_contracts": [
    { file: "steps/083_data_contracts/implementation/exercises/data_contracts/01_contracts.py", label: "01_contracts.py", command: "pytest steps/083_data_contracts/tests/exercise_tests/data_contracts/test_contracts.py -q" },
  ],
  "084_pandas_excel": [
    { file: "steps/084_pandas_excel/implementation/exercises/pandas_excel/01_pandas_basics.py", label: "01_pandas_basics.py", command: "pytest steps/084_pandas_excel/tests/exercise_tests/pandas_excel/test_pandas_basics.py -q" },
  ],
  "085_log_analysis": [
    { file: "steps/085_log_analysis/implementation/exercises/log_analysis/01_jsonl_logs.py", label: "01_jsonl_logs.py", command: "pytest steps/085_log_analysis/tests/exercise_tests/log_analysis/test_jsonl_logs.py -q" },
  ],
  "086_mongo_ops_schema": [
    { file: "steps/086_mongo_ops_schema/implementation/exercises/mongo_ops_schema/01_mongo_ops.py", label: "01_mongo_ops.py", command: "pytest steps/086_mongo_ops_schema/tests/exercise_tests/mongo_ops_schema/test_mongo_ops.py -q" },
  ],
  "087_worker_dead_letter": [
    { file: "steps/087_worker_dead_letter/implementation/exercises/worker_dead_letter/01_worker.py", label: "01_worker.py", command: "pytest steps/087_worker_dead_letter/tests/exercise_tests/worker_dead_letter/test_worker.py -q" },
  ],
  "088_data_analysis_stats": [
    { file: "steps/088_data_analysis_stats/implementation/exercises/data_analysis_stats/01_stats.py", label: "01_stats.py", command: "pytest steps/088_data_analysis_stats/tests/exercise_tests/data_analysis_stats/test_stats.py -q" },
  ],
  "089_model_mapping": [
    { file: "steps/089_model_mapping/implementation/exercises/model_mapping/01_model_registry.py", label: "01_model_registry.py", command: "pytest steps/089_model_mapping/tests/exercise_tests/model_mapping/test_01_model_registry.py steps/089_model_mapping/tests/exercise_tests/model_mapping/test_02_config_loader.py -q" },
    { file: "steps/089_model_mapping/implementation/exercises/model_mapping/02_config_loader.py", label: "02_config_loader.py", command: "pytest steps/089_model_mapping/tests/exercise_tests/model_mapping/test_02_config_loader.py -q" },
  ],
  "090_ai_cost_control": [
    { file: "steps/090_ai_cost_control/implementation/exercises/ai_cost_control/01_token_budget.py", label: "01_token_budget.py", command: "pytest steps/090_ai_cost_control/tests/exercise_tests/ai_cost_control/test_token_budget.py -q" },
  ],
  "091_google_ai": [
    { file: "steps/091_google_ai/implementation/exercises/google_ai/01_genai_config.py", label: "01_genai_config.py", command: "pytest steps/091_google_ai/tests/exercise_tests/google_ai/test_01_genai_config.py -q" },
  ],
  "094_vector_search_basics": [
    { file: "steps/094_vector_search_basics/implementation/exercises/vector_search/01_vector_search.py", label: "01_vector_search.py", command: "pytest steps/094_vector_search_basics/tests/exercise_tests/vector_search/test_vector_search.py -q" },
  ],
  "095_rag_basics": [
    { file: "steps/095_rag_basics/implementation/exercises/rag_basics/01_retrieval.py", label: "01_retrieval.py", command: "pytest steps/095_rag_basics/tests/exercise_tests/rag_basics/test_retrieval.py -q" },
  ],
  "096_rag_deep": [
    { file: "steps/096_rag_deep/implementation/exercises/rag_deep/01_documents.py", label: "01_documents.py", command: "pytest steps/096_rag_deep/tests/exercise_tests/rag_deep/test_01_documents.py steps/096_rag_deep/tests/exercise_tests/rag_deep/test_02_retriever.py -q" },
    { file: "steps/096_rag_deep/implementation/exercises/rag_deep/05_citations.py", label: "05_citations.py", command: "pytest steps/096_rag_deep/tests/exercise_tests/rag_deep/test_05_citations.py -q" },
  ],
  "097_rag_advanced": [
    { file: "steps/097_rag_advanced/implementation/exercises/rag_advanced/01_rag_rerank.py", label: "01_rag_rerank.py", command: "pytest steps/097_rag_advanced/tests/exercise_tests/rag_advanced/test_rag_rerank.py -q" },
  ],
  "098_rag_practice": [
    { file: "steps/098_rag_practice/implementation/exercises/rag_practice/01_rag_quality.py", label: "01_rag_quality.py", command: "pytest steps/098_rag_practice/tests/exercise_tests/rag_practice/test_rag_quality.py -q" },
  ],
  "099_llm_ops": [
    { file: "steps/099_llm_ops/implementation/exercises/llm_ops/01_llm_ops.py", label: "01_llm_ops.py", command: "pytest steps/099_llm_ops/tests/exercise_tests/llm_ops/test_llm_ops.py -q" },
  ],
  "100_ai_streaming": [
    { file: "steps/100_ai_streaming/implementation/exercises/ai_streaming/01_streaming.py", label: "01_streaming.py", command: "pytest steps/100_ai_streaming/tests/exercise_tests/ai_streaming/test_streaming.py -q" },
  ],
  "101_batch_inference": [
    { file: "steps/101_batch_inference/implementation/exercises/batch_inference/01_batch_input.py", label: "01_batch_input.py", command: "pytest steps/101_batch_inference/tests/exercise_tests/batch_inference/test_01_batch_input.py -q" },
    { file: "steps/101_batch_inference/implementation/exercises/batch_inference/02_vertex_batch_config.py", label: "02_vertex_batch_config.py", command: "pytest steps/101_batch_inference/tests/exercise_tests/batch_inference/test_02_vertex_batch_config.py -q" },
  ],
  "102_ai_evaluation": [
    { file: "steps/102_ai_evaluation/implementation/exercises/ai_evaluation/01_metrics.py", label: "01_metrics.py", command: "pytest steps/102_ai_evaluation/tests/exercise_tests/ai_evaluation/test_metrics.py -q" },
  ],
  "103_ai_agents": [
    { file: "steps/103_ai_agents/implementation/exercises/ai_agents/01_agent_loop.py", label: "01_agent_loop.py", command: "pytest steps/103_ai_agents/tests/exercise_tests/ai_agents/test_agent_loop.py -q" },
  ],
  "104_prompt_templates": [
    { file: "steps/104_prompt_templates/implementation/exercises/prompt_templates/01_templates.py", label: "01_templates.py", command: "pytest steps/104_prompt_templates/tests/exercise_tests/prompt_templates/test_templates.py -q" },
  ],
  "105_prompt_injection_defense": [
    { file: "steps/105_prompt_injection_defense/implementation/exercises/prompt_injection/01_defense.py", label: "01_defense.py", command: "pytest steps/105_prompt_injection_defense/tests/exercise_tests/prompt_injection/test_defense.py -q" },
  ],
  "106_structured_output_parsing": [
    { file: "steps/106_structured_output_parsing/implementation/exercises/structured_output/01_parse_validate.py", label: "01_parse_validate.py", command: "pytest steps/106_structured_output_parsing/tests/exercise_tests/structured_output/test_parse_validate.py -q" },
  ],
  "107_tool_calling_contracts": [
    { file: "steps/107_tool_calling_contracts/implementation/exercises/tool_calling_contracts/01_tool_contracts.py", label: "01_tool_contracts.py", command: "pytest steps/107_tool_calling_contracts/tests/exercise_tests/tool_calling_contracts/test_tool_contracts.py -q" },
  ],
  "108_conversation_memory": [
    { file: "steps/108_conversation_memory/implementation/exercises/conversation_memory/01_memory.py", label: "01_memory.py", command: "pytest steps/108_conversation_memory/tests/exercise_tests/conversation_memory/test_memory.py -q" },
  ],
  "109_embedding_chunk_metadata": [
    { file: "steps/109_embedding_chunk_metadata/implementation/exercises/embedding_metadata/01_chunks.py", label: "01_chunks.py", command: "pytest steps/109_embedding_chunk_metadata/tests/exercise_tests/embedding_metadata/test_chunks.py -q" },
  ],
  "110_vector_db_index_design": [
    { file: "steps/110_vector_db_index_design/implementation/exercises/vector_index_design/01_index_config.py", label: "01_index_config.py", command: "pytest steps/110_vector_db_index_design/tests/exercise_tests/vector_index_design/test_index_config.py -q" },
  ],
  "111_rag_query_rewriting": [
    { file: "steps/111_rag_query_rewriting/implementation/exercises/rag_query_rewriting/01_rewrite.py", label: "01_rewrite.py", command: "pytest steps/111_rag_query_rewriting/tests/exercise_tests/rag_query_rewriting/test_rewrite.py -q" },
  ],
  "112_rag_citation_verification": [
    { file: "steps/112_rag_citation_verification/implementation/exercises/rag_citation_verification/01_citations.py", label: "01_citations.py", command: "pytest steps/112_rag_citation_verification/tests/exercise_tests/rag_citation_verification/test_citations.py -q" },
  ],
  "113_ai_safety_filters": [
    { file: "steps/113_ai_safety_filters/implementation/exercises/ai_safety_filters/01_safety.py", label: "01_safety.py", command: "pytest steps/113_ai_safety_filters/tests/exercise_tests/ai_safety_filters/test_safety.py -q" },
  ],
  "114_model_fallback_routing": [
    { file: "steps/114_model_fallback_routing/implementation/exercises/model_fallback_routing/01_routing.py", label: "01_routing.py", command: "pytest steps/114_model_fallback_routing/tests/exercise_tests/model_fallback_routing/test_routing.py -q" },
  ],
  "115_ai_observability_traces": [
    { file: "steps/115_ai_observability_traces/implementation/exercises/ai_observability/01_traces.py", label: "01_traces.py", command: "pytest steps/115_ai_observability_traces/tests/exercise_tests/ai_observability/test_traces.py -q" },
  ],
  "116_ai_regression_dataset": [
    { file: "steps/116_ai_regression_dataset/implementation/exercises/ai_regression_dataset/01_dataset.py", label: "01_dataset.py", command: "pytest steps/116_ai_regression_dataset/tests/exercise_tests/ai_regression_dataset/test_dataset.py -q" },
  ],
  "117_domain_ai_requirements": [
    { file: "steps/117_domain_ai_requirements/implementation/exercises/domain_ai_requirements/01_requirements.py", label: "01_requirements.py", command: "pytest steps/117_domain_ai_requirements/tests/exercise_tests/domain_ai_requirements/test_requirements.py -q" },
  ],
  "118_domain_knowledge_taxonomy": [
    { file: "steps/118_domain_knowledge_taxonomy/implementation/exercises/domain_taxonomy/01_taxonomy.py", label: "01_taxonomy.py", command: "pytest steps/118_domain_knowledge_taxonomy/tests/exercise_tests/domain_taxonomy/test_taxonomy.py -q" },
  ],
  "119_domain_dataset_curation": [
    { file: "steps/119_domain_dataset_curation/implementation/exercises/domain_dataset_curation/01_curation.py", label: "01_curation.py", command: "pytest steps/119_domain_dataset_curation/tests/exercise_tests/domain_dataset_curation/test_curation.py -q" },
  ],
  "120_domain_evaluation_rubric": [
    { file: "steps/120_domain_evaluation_rubric/implementation/exercises/domain_eval_rubric/01_rubric.py", label: "01_rubric.py", command: "pytest steps/120_domain_evaluation_rubric/tests/exercise_tests/domain_eval_rubric/test_rubric.py -q" },
  ],
  "121_expert_feedback_loop": [
    { file: "steps/121_expert_feedback_loop/implementation/exercises/expert_feedback_loop/01_feedback.py", label: "01_feedback.py", command: "pytest steps/121_expert_feedback_loop/tests/exercise_tests/expert_feedback_loop/test_feedback.py -q" },
  ],
  "122_domain_rag_blueprint": [
    { file: "steps/122_domain_rag_blueprint/implementation/exercises/domain_rag_blueprint/01_blueprint.py", label: "01_blueprint.py", command: "pytest steps/122_domain_rag_blueprint/tests/exercise_tests/domain_rag_blueprint/test_blueprint.py -q" },
  ],
  "123_finetuning_dataset_prep": [
    { file: "steps/123_finetuning_dataset_prep/implementation/exercises/finetuning_dataset_prep/01_prep.py", label: "01_prep.py", command: "pytest steps/123_finetuning_dataset_prep/tests/exercise_tests/finetuning_dataset_prep/test_prep.py -q" },
  ],
  "124_domain_guardrails_policy": [
    { file: "steps/124_domain_guardrails_policy/implementation/exercises/domain_guardrails/01_policy.py", label: "01_policy.py", command: "pytest steps/124_domain_guardrails_policy/tests/exercise_tests/domain_guardrails/test_policy.py -q" },
  ],
  "125_specialized_ai_api_design": [
    { file: "steps/125_specialized_ai_api_design/implementation/exercises/specialized_ai_api_design/01_api_contract.py", label: "01_api_contract.py", command: "pytest steps/125_specialized_ai_api_design/tests/exercise_tests/specialized_ai_api_design/test_api_contract.py -q" },
  ],
  "126_domain_ai_release_checklist": [
    { file: "steps/126_domain_ai_release_checklist/implementation/exercises/domain_ai_release_checklist/01_checklist.py", label: "01_checklist.py", command: "pytest steps/126_domain_ai_release_checklist/tests/exercise_tests/domain_ai_release_checklist/test_checklist.py -q" },
  ],
  "127_ai_dataset_versioning": [
    { file: "steps/127_ai_dataset_versioning/implementation/exercises/ai_dataset_versioning/01_dataset.py", label: "01_dataset.py", command: "pytest steps/127_ai_dataset_versioning/tests/exercise_tests/ai_dataset_versioning/test_dataset.py -q" },
  ],
  "128_ai_ab_drift": [
    { file: "steps/128_ai_ab_drift/implementation/exercises/ai_ab_drift/01_ab_drift.py", label: "01_ab_drift.py", command: "pytest steps/128_ai_ab_drift/tests/exercise_tests/ai_ab_drift/test_ab_drift.py -q" },
  ],
  "129_rag_ops_quality": [
    { file: "steps/129_rag_ops_quality/implementation/exercises/rag_ops_quality/01_rag_ops.py", label: "01_rag_ops.py", command: "pytest steps/129_rag_ops_quality/tests/exercise_tests/rag_ops_quality/test_rag_ops.py -q" },
  ],
  "130_fastapi_ai": [
    { file: "steps/130_fastapi_ai/implementation/exercises/fastapi_ai_app/ai_client.py", label: "ai_client.py", command: "pytest steps/130_fastapi_ai/tests -q" },
    { file: "steps/130_fastapi_ai/implementation/exercises/fastapi_ai_app/main.py", label: "main.py", command: "pytest steps/130_fastapi_ai/tests/exercise_tests/fastapi_ai_app/test_fastapi_ai_app.py -q" },
    { file: "steps/130_fastapi_ai/implementation/exercises/fastapi_ai_app/service.py", label: "service.py", command: "pytest steps/130_fastapi_ai/tests/exercise_tests/fastapi_ai_app/test_fastapi_ai_app.py -q" },
  ],
  "132_review_comments": [
    { file: "steps/132_review_comments/implementation/exercises/review_comments/01_review_comment.py", label: "01_review_comment.py", command: "pytest steps/132_review_comments/tests/exercise_tests/review_comments/test_review_comment.py -q" },
  ],
  "133_api_compatibility_design": [
    { file: "steps/133_api_compatibility_design/implementation/exercises/api_compatibility_design/01_compatibility.py", label: "01_compatibility.py", command: "pytest steps/133_api_compatibility_design/tests/exercise_tests/api_compatibility_design/test_compatibility.py -q" },
  ],
  "135_cli_tools": [
    { file: "steps/135_cli_tools/implementation/exercises/cli_tools/01_argparse_cli.py", label: "01_argparse_cli.py", command: "pytest steps/135_cli_tools/tests/exercise_tests/cli_tools/test_argparse_cli.py -q" },
  ],
  "136_ci_debugging": [
    { file: "steps/136_ci_debugging/implementation/exercises/ci_debugging/01_actions_log.py", label: "01_actions_log.py", command: "pytest steps/136_ci_debugging/tests/exercise_tests/ci_debugging/test_actions_log.py -q" },
  ],
  "137_docker_ops": [
    { file: "steps/137_docker_ops/implementation/exercises/docker_ops/01_health_env.py", label: "01_health_env.py", command: "pytest steps/137_docker_ops/tests/exercise_tests/docker_ops/test_health_env.py -q" },
  ],
  "138_git_workflow": [
    { file: "steps/138_git_workflow/implementation/exercises/git_workflow/01_status_parser.py", label: "01_status_parser.py", command: "pytest steps/138_git_workflow/tests/exercise_tests/git_workflow/test_status_parser.py -q" },
  ],
  "139_feature_flags": [
    { file: "steps/139_feature_flags/implementation/exercises/feature_flags/01_flags.py", label: "01_flags.py", command: "pytest steps/139_feature_flags/tests/exercise_tests/feature_flags/test_flags.py -q" },
  ],
  "140_security_scanning": [
    { file: "steps/140_security_scanning/implementation/exercises/security_scanning/01_security.py", label: "01_security.py", command: "pytest steps/140_security_scanning/tests/exercise_tests/security_scanning/test_security.py -q" },
  ],
  "141_observability_slo": [
    { file: "steps/141_observability_slo/implementation/exercises/observability_slo/01_slo.py", label: "01_slo.py", command: "pytest steps/141_observability_slo/tests/exercise_tests/observability_slo/test_slo.py -q" },
  ],
  "142_deploy_release_strategy": [
    { file: "steps/142_deploy_release_strategy/implementation/exercises/deploy_release_strategy/01_release.py", label: "01_release.py", command: "pytest steps/142_deploy_release_strategy/tests/exercise_tests/deploy_release_strategy/test_release.py -q" },
  ],
};
