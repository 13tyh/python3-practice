# Exercises

ここは「読む」より「書く」ための場所です。

通常の `pytest -q` では実行されません。基礎練習を確認する時だけ次を使います。

```bash
pytest exercise_tests -q
```

プロセス系だけ確認する:

```bash
pytest exercise_tests/processes -q
```

API / async / Google AI 系だけ確認する:

```bash
pytest exercise_tests/network_api -q
pytest exercise_tests/async_python -q
pytest exercise_tests/google_ai -q
```

model / service / router の分け方:

```bash
pytest exercise_tests/app_layers -q
```

応用パート:

```bash
pytest exercise_tests/advanced -q
```

logger とバッチ推論:

```bash
pytest exercise_tests/logging_python -q
pytest exercise_tests/batch_inference -q
```

型と FastAPI:

```bash
pytest exercise_tests/typing_deep -q
pytest exercise_tests/fastapi_app -q
```

FastAPI で AI 系 API を作る:

```bash
pytest exercise_tests/fastapi_ai_app -q
```

ここでは endpoint だけでなく、settings、prompt template、fake generator、service 分割も練習する。

DB export / docs PDF:

```bash
pytest exercise_tests/file_db_export -q
pytest exercise_tests/docs_pdf -q
```

分析系:

```bash
pytest exercise_tests/data_analysis -q
pytest exercise_tests/pandas_excel -q
pytest exercise_tests/log_analysis -q
pytest exercise_tests/mongo_aggregation -q
pytest exercise_tests/ai_evaluation -q
pytest exercise_tests/rag_basics -q
```

model mapping / RAG 深掘り:

```bash
pytest exercise_tests/model_mapping -q
pytest exercise_tests/rag_deep -q
```

運用寄りのアプリ実装:

```bash
pytest exercise_tests/auth -q
pytest exercise_tests/error_handling -q
pytest exercise_tests/async_fastapi -q
pytest exercise_tests/job_queue -q
pytest exercise_tests/sql_basics -q
pytest exercise_tests/cache -q
pytest exercise_tests/security -q
pytest exercise_tests/ai_streaming -q
pytest exercise_tests/rag_practice -q
```

チーム開発・運用寄り:

```bash
pytest exercise_tests/dependency_injection -q
pytest exercise_tests/transactions -q
pytest exercise_tests/api_client -q
pytest exercise_tests/observability -q
pytest exercise_tests/pydantic_validation -q
pytest exercise_tests/package_design -q
pytest exercise_tests/design_patterns -q
pytest exercise_tests/datetime_timezone -q
pytest exercise_tests/performance -q
pytest exercise_tests/concurrency_practice -q
pytest exercise_tests/llm_ops -q
```

さらに実務寄り:

```bash
pytest exercise_tests/testing_deep -q
pytest exercise_tests/api_design -q
pytest exercise_tests/mongo_deep -q
pytest exercise_tests/rag_advanced -q
pytest exercise_tests/ai_agents -q
pytest exercise_tests/refactoring -q
```

N+1 / performance:

```bash
pytest exercise_tests/n_plus_one_performance -q
```

重要な設計思考:

```bash
pytest exercise_tests/core_design_thinking -q
```

深掘り追加:

```bash
pytest exercise_tests/fastapi_ai_app/test_errors_usage.py -q
pytest exercise_tests/rag_deep/test_04_prompting.py -q
pytest exercise_tests/rag_deep/test_05_citations.py -q
pytest exercise_tests/testing_deep/test_monkeypatch_env.py -q
pytest exercise_tests/mongo_deep/test_migration.py -q
pytest exercise_tests/refactoring/test_code_smells.py -q
```

進め方:

1. `exercises/basics/01_values.py` から順に TODO を埋める
2. 対応する `exercise_tests/basics/test_*.py` を見る
3. テストが落ちたら、エラー文から期待値と実際の値を読む
4. AI に答えを出させた場合も、なぜその答えになるか説明する

基礎は `01_values.py` から `33_oop_basic.py` まである。詰まったら1ファイルずつ実行する。

```bash
pytest exercise_tests/basics/test_18_bool_none.py -q
```

基礎反復:

```bash
pytest exercise_tests/basics_repetition -q
```
