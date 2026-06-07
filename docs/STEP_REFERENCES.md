# Step References

番号順に進めるためのコメントと参考URL。

| Step | コメント | 参考URL |
| --- | --- | --- |
| `00_environment` | Docker / Poetry / pytest / ruff / mypy の役割を分ける。 | https://python-poetry.org/docs/ / https://docs.pytest.org/en/stable/ |
| `01_syntax` | 入力、処理、戻り値、例外で関数を読む。 | https://docs.python.org/3/tutorial/ |
| `02_typing_deep` | 型は設計意図。`None` と `Protocol` を特に意識する。 | https://docs.python.org/3/library/typing.html |
| `03_files` | encoding、path、上書き、存在しないファイルを見る。 | https://docs.python.org/3/library/pathlib.html |
| `04_datetime_timezone` | UTC保存、JST表示、aware/naive を混ぜない。 | https://docs.python.org/3/library/datetime.html |
| `05_testing_deep` | fixture、monkeypatch、fake client で外部依存を切る。 | https://docs.pytest.org/en/stable/reference/fixtures.html |
| `06_core_design_thinking` | 冪等性、境界値、不変条件、状態遷移、正規化、fail fast を処理で学ぶ。 | https://martinfowler.com/bliki/TwoHardThings.html |
| `07_logging` | `print` ではなく logger。secret は出さない。 | https://docs.python.org/3/library/logging.html |
| `08_observability` | request id、structured log、metrics を残す。 | https://opentelemetry.io/docs/languages/python/ |
| `09_project_reading` | テスト、public関数、境界値、実装の順で読む。 | https://docs.pytest.org/en/stable/ |
| `10_refactoring` | 仕様を変えず構造を変える。先にテストを書く。 | https://refactoring.guru/refactoring |
| `11_package_design` | import の向きと circular import を意識する。 | https://docs.python.org/3/tutorial/modules.html |
| `12_app_layers` | model は形、service は業務ロジック、router は入出力。 | https://fastapi.tiangolo.com/tutorial/bigger-applications/ |
| `13_design_patterns` | 差し替えポイントを作るために pattern を使う。 | https://refactoring.guru/design-patterns/python |
| `14_advanced` | 設定、Repository、例外、ページング、cache、retry を読む。 | https://docs.python.org/3/library/exceptions.html |
| `15_pydantic_validation` | API契約を schema と validator で守る。 | https://docs.pydantic.dev/latest/ |
| `16_fastapi` | 型ヒントと Pydantic を中心に API を作る。 | https://fastapi.tiangolo.com/ |
| `17_dependency_injection` | repository / client を fake に差し替えられる設計にする。 | https://fastapi.tiangolo.com/tutorial/dependencies/ |
| `18_auth` | 認証は誰か、認可は何をしてよいか。 | https://fastapi.tiangolo.com/tutorial/security/ |
| `19_error_handling` | domain error を HTTP error に変換する。 | https://fastapi.tiangolo.com/tutorial/handling-errors/ |
| `20_security` | path traversal、secret leakage、prompt injection を疑う。 | https://owasp.org/www-project-top-10-for-large-language-model-applications/ |
| `21_api_design` | pagination、sorting、error format、idempotency を設計する。 | https://fastapi.tiangolo.com/tutorial/query-params/ |
| `22_network_api` | method、URL、headers、params、body、status、timeout で読む。 | https://www.python-httpx.org/ |
| `23_api_client` | timeout、retry、backoff、rate limit を client に閉じ込める。 | https://www.python-httpx.org/advanced/timeouts/ |
| `24_async` | async は I/O 待ちの並行処理。CPU処理とは分ける。 | https://docs.python.org/3/library/asyncio.html |
| `25_async_fastapi` | FastAPI の async endpoint と I/O 待ちを理解する。 | https://fastapi.tiangolo.com/async/ |
| `26_concurrency_practice` | semaphore、timeout、cancellation を扱う。 | https://docs.python.org/3/library/asyncio-sync.html |
| `27_processes` | subprocess と multiprocessing の違いを理解する。 | https://docs.python.org/3/library/subprocess.html |
| `28_performance` | generator、chunk、計測で大量処理に備える。 | https://docs.python.org/3/library/profile.html |
| `29_n_plus_one_performance` | loop 内 DB/API 呼び出しを見つけ、bulk取得と map 化に直す。 | https://www.mongodb.com/docs/manual/reference/operator/query/in/ |
| `30_sql` | SQLite で CRUD と transaction の基本をつかむ。 | https://docs.python.org/3/library/sqlite3.html |
| `31_mongo` | document、query、projection、index をセットで読む。 | https://www.mongodb.com/docs/languages/python/pymongo-driver/current/ |
| `32_mongosh_commands` | mongosh で検索、更新、集計、index、explain、seed確認を行う。 | https://www.mongodb.com/docs/mongodb-shell/ |
| `33_mongo_aggregation` | `$match`、`$group`、`$lookup`、`$sort` と index を見る。 | https://www.mongodb.com/docs/manual/aggregation/ |
| `34_mongo_deep` | index、compound index、upsert、explain を扱う。 | https://www.mongodb.com/docs/languages/python/pymongo-driver/current/indexes/ |
| `35_transactions` | 複数書き込みの途中失敗と rollback を考える。 | https://www.mongodb.com/docs/manual/core/transactions/ |
| `36_cache` | cache key、TTL、invalidation を設計する。 | https://redis.io/docs/latest/ |
| `37_job_queue` | status、attempts、retry、result を持つ job を考える。 | https://docs.python.org/3/library/queue.html |
| `38_file_db_export` | DB抽出、projection、CSV header、encoding を扱う。 | https://docs.python.org/3/library/csv.html |
| `39_docs_pdf` | 分割単位、ファイル名、文字化け、ページ順を見る。 | https://pypdf.readthedocs.io/en/stable/ |
| `40_data_analysis` | 欠損、型、重複、集計前処理を固める。 | https://pandas.pydata.org/docs/ |
| `41_pandas_excel` | CSV/Excel、sheet、列型、欠損を扱う。 | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html |
| `42_log_analysis` | JSONLログから error rate と latency を見る。 | https://jsonlines.org/ |
| `43_model_mapping` | deployment_name と model_name を分けてログに残す。 | https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource |
| `44_google_ai` | Gemini API と Vertex AI の認証・project・location を分ける。 | https://ai.google.dev/gemini-api/docs |
| `45_langchain` | prompt、model、parser、chain を分けて読む。 | https://docs.langchain.com/oss/python |
| `46_langgraph` | state、node、edge、END を図にできるようにする。 | https://langchain-ai.github.io/langgraph/ |
| `47_rag_basics` | chunk、retrieval、context を分けて考える。 | https://docs.langchain.com/oss/python/langchain/retrieval |
| `48_rag_deep` | overlap、score threshold、citation、answerable 判定を扱う。 | https://python.langchain.com/docs/concepts/retrieval/ |
| `49_rag_advanced` | hybrid search、metadata filtering、rerank を試す。 | https://scikit-learn.org/stable/modules/metrics.html |
| `50_rag_practice` | answerable / unanswerable と citation 必須化を練習する。 | https://owasp.org/www-project-top-10-for-large-language-model-applications/ |
| `51_llm_ops` | prompt version、fallback、guardrails、token/cost を管理する。 | https://platform.openai.com/docs/models |
| `52_ai_streaming` | SSE と StreamingResponse の形を理解する。 | https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse |
| `53_batch_inference` | 大量推論は入力/出力保存、失敗行、非同期完了を考える。 | https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-gemini |
| `54_ai_evaluation` | 正解率、失敗理由、prompt/model 別比較を記録する。 | https://scikit-learn.org/stable/modules/model_evaluation.html |
| `55_ai_agents` | tool calling、planner、memory、human review を分ける。 | https://docs.langchain.com/oss/python/langchain/agents |
| `56_fastapi_ai` | AI呼び出しは router ではなく service に閉じ込める。 | https://fastapi.tiangolo.com/advanced/testing-dependencies/ |
| `57_ai_review` | AI出力の仕様差分、境界値、テスト不足を指摘する。 | https://docs.pytest.org/en/stable/ |
| `58_capstone` | FastAPI、DB、AI、ログ、評価を統合する。 | https://fastapi.tiangolo.com/tutorial/bigger-applications/ |
