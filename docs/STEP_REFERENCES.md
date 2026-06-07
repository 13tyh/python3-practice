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
| `59_cli_tools` | 実務CLIは入力、検証、内部設定への変換を分ける。 | https://docs.python.org/3/library/argparse.html |
| `60_static_typing_practice` | union型は処理前に絞り込み、型ヒントを実データと一致させる。 | https://mypy.readthedocs.io/en/stable/type_narrowing.html |
| `61_domain_modeling` | 業務ルールはdict処理に埋めず、domain modelへ寄せる。 | https://docs.python.org/3/library/dataclasses.html |
| `62_api_pagination_deep` | cursor paginationは安定sortとnext_cursorの意味を固定する。 | https://jsonapi.org/profiles/ethanresnick/cursor-pagination/ |
| `63_etl_pipeline` | extract、transform、loadを分け、大量データをstreamで扱う。 | https://docs.python.org/3/howto/functional.html#generators |
| `64_resilience_patterns` | retryはstatus、attempt、backoff、上限をセットで設計する。 | https://cloud.google.com/architecture/framework/reliability/retry-transient-errors |
| `65_webhooks_events` | webhookは署名検証とevent_idによる冪等性が重要。 | https://docs.python.org/3/library/hmac.html |
| `66_ci_debugging` | CI失敗はlint、format、test、env差分に分けて読む。 | https://docs.github.com/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs |
| `67_docker_ops` | healthcheck、env、logs、profilesを運用調査の入口にする。 | https://docs.docker.com/compose/compose-file/05-services/#healthcheck |
| `68_vector_search_basics` | RAG検索の土台としてcosine similarityとtop-kを理解する。 | https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity |
| `69_ai_cost_control` | token budget、model limit、deployment mappingで費用と品質を判断する。 | https://platform.openai.com/tokenizer |
| `70_schema_evolution` | migrationは再実行可能性、dry-run、新旧schema互換性を確認する。 | https://www.mongodb.com/docs/manual/core/schema-validation/ |
| `71_git_workflow` | status、ahead/behind、差分確認をcommit前の判断材料にする。 | https://git-scm.com/docs/git-status |
| `72_review_comments` | レビューはseverity、問題、修正案を分けて具体化する。 | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests |
| `73_feature_flags` | 段階リリースと緊急停止のためにflagを設計する。 | https://martinfowler.com/articles/feature-toggles.html |
| `74_settings_secrets` | 必須設定、secret、公開可能な設定を分ける。 | https://12factor.net/config |
| `75_rate_limiting` | APIやAI呼び出しを守るためにwindowとlimitを決める。 | https://cloud.google.com/architecture/rate-limiting-strategies-techniques |
| `76_background_tasks` | job状態、idempotency key、失敗記録を設計する。 | https://fastapi.tiangolo.com/tutorial/background-tasks/ |
| `77_scheduler_cron` | 定期実行はdue判定と再実行安全性をセットで考える。 | https://docs.python.org/3/library/datetime.html |
| `78_data_contracts` | producer/consumer間のfieldとversion互換性を見る。 | https://docs.pydantic.dev/latest/concepts/models/ |
| `79_openapi_contract` | OpenAPIからpath、method、response codeを読み取る。 | https://spec.openapis.org/oas/latest.html |
| `80_mocking_external_services` | 外部APIはfake clientで置き換え、呼び出し履歴を検証する。 | https://docs.pytest.org/en/stable/how-to/monkeypatch.html |
| `81_property_based_thinking` | 具体例だけでなく冪等性、正規化、順序安定を検証する。 | https://hypothesis.readthedocs.io/en/latest/ |
| `82_memory_profiling` | メモリ上限からchunk sizeを決め、一括読み込みを避ける。 | https://docs.python.org/3/library/tracemalloc.html |
| `83_streaming_files_large` | 大きいファイルはline単位のgeneratorで扱う。 | https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files |
| `84_debugging_deep` | tracebackから例外名、file、line、再現条件を整理する。 | https://docs.python.org/3/library/traceback.html |
| `85_architecture_decision_records` | 設計判断はContext、Decision、Consequencesで残す。 | https://adr.github.io/ |
| `86_boolean_logic` | 複数条件はtruthy/falsyと優先順位を意識して読む。 | https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not |
| `87_string_formatting_parsing` | f-string、split、strip、joinは実務の文字列処理の土台。 | https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals |
| `88_sequence_unpacking` | tuple unpackingと`*rest`で戻り値やpairを読みやすく扱う。 | https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences |
| `89_function_arguments` | default、keyword-only、option dictで関数の入口を設計する。 | https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions |
| `90_scope_modules` | local変数、module定数、public関数の境界を意識する。 | https://docs.python.org/3/tutorial/modules.html |
| `91_list_methods` | append/extendと破壊的変更の違いを確認する。 | https://docs.python.org/3/tutorial/datastructures.html#more-on-lists |
| `92_dict_methods` | get、更新、count処理でKeyErrorを避ける。 | https://docs.python.org/3/tutorial/datastructures.html#dictionaries |
| `93_set_operations` | unique化、共通集合、差集合でtagや権限を比較する。 | https://docs.python.org/3/tutorial/datastructures.html#sets |
| `94_comprehension_deep` | list/dict/set内包表記を読める粒度で使う。 | https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions |
| `95_iterable_generator_basics` | generatorとyieldで大量データを少しずつ扱う。 | https://docs.python.org/3/howto/functional.html#generators |
| `96_pathlib_glob` | Path、suffix、nameでファイルパスを安全に扱う。 | https://docs.python.org/3/library/pathlib.html |
| `97_custom_exceptions` | 独自例外でvalidation失敗と内部エラーを分ける。 | https://docs.python.org/3/tutorial/errors.html |
| `98_prompt_templates` | promptはtemplate、変数、versionを分けて管理する。 | https://docs.langchain.com/oss/python/langchain/prompts |
| `99_prompt_injection_defense` | untrusted contextを命令として扱わず、injection疑いを検出する。 | https://owasp.org/www-project-top-10-for-large-language-model-applications/ |
| `100_structured_output_parsing` | AI出力はJSON/schemaとして検証してから採用する。 | https://docs.pydantic.dev/latest/ |
| `101_tool_calling_contracts` | tool callingはallowlistとarguments検証で制限する。 | https://docs.langchain.com/oss/python/langchain/tools |
| `102_conversation_memory` | 会話履歴はsystemを保持しつつtoken budget内にtrimする。 | https://docs.langchain.com/oss/python/langchain/short-term-memory |
| `103_embedding_chunk_metadata` | chunk id、source、metadataを持たせcitation可能にする。 | https://python.langchain.com/docs/concepts/text_splitters/ |
| `104_vector_db_index_design` | vector dimension、metric、metadata filterを設計する。 | https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/ |
| `105_rag_query_rewriting` | 検索queryは正規化、synonym、metadata filterを分けて作る。 | https://docs.langchain.com/oss/python/langchain/retrieval |
| `106_rag_citation_verification` | citationが実在chunkを指すか確認し、根拠なし回答を防ぐ。 | https://python.langchain.com/docs/concepts/retrieval/ |
| `107_ai_safety_filters` | PII mask、unsafe intent検出、安全な拒否理由を作る。 | https://owasp.org/www-project-top-10-for-large-language-model-applications/ |
| `108_model_fallback_routing` | fallbackはtask、失敗種別、上限を決めてから行う。 | https://docs.langchain.com/oss/python/langchain/model_io |
| `109_ai_observability_traces` | AI呼び出しはmodel、prompt_version、latency、token/costを追跡する。 | https://opentelemetry.io/docs/languages/python/ |
| `110_ai_regression_dataset` | prompt/model変更は回帰datasetで比較する。 | https://scikit-learn.org/stable/modules/model_evaluation.html |
| `111_domain_ai_requirements` | 特化型AIは「誰の何を助けるか」と「答えてはいけない範囲」を先に決める。 | https://pair.withgoogle.com/guidebook/ |
| `112_domain_knowledge_taxonomy` | 業務用語、判断ルール、例外、根拠資料を分類して検索と評価に使える形にする。 | https://www.w3.org/TR/skos-primer/ |
| `113_domain_dataset_curation` | 専門データは重複、古さ、PII、偏りを取り除いてから学習や評価に使う。 | https://www.nist.gov/itl/ai-risk-management-framework |
| `114_domain_evaluation_rubric` | 正しさだけでなく根拠、拒否、業務手順、安全性を評価軸にする。 | https://scikit-learn.org/stable/modules/model_evaluation.html |
| `115_expert_feedback_loop` | 専門家レビューを理由付きで残し、prompt/RAG/fine-tuningのどこを直すか判断する。 | https://docs.langchain.com/oss/python/langsmith/evaluation |
| `116_domain_rag_blueprint` | 特化型RAGはsource、chunk、metadata、citation、更新頻度を設計する。 | https://python.langchain.com/docs/concepts/retrieval/ |
| `117_finetuning_dataset_prep` | fine-tuning用データは入出力形式、拒否例、禁止情報、検証をそろえる。 | https://platform.openai.com/docs/guides/fine-tuning |
| `118_domain_guardrails_policy` | 業務範囲外、危険な指示、根拠不足、PIIを扱う方針をコード化する。 | https://owasp.org/www-project-top-10-for-large-language-model-applications/ |
| `119_specialized_ai_api_design` | APIはrequest、response、trace、evaluation、fallback理由を返せる形にする。 | https://fastapi.tiangolo.com/tutorial/bigger-applications/ |
| `120_domain_ai_release_checklist` | release前に評価、ログ、監視、rollback、human reviewを確認する。 | https://cloud.google.com/architecture/framework |
| `121_collections_deep` | `Counter`、`defaultdict`、`deque`で集計とgroup化を簡潔に書く。 | https://docs.python.org/3/library/collections.html |
| `122_itertools_functools` | iterable処理、関数の部分適用、cacheの使いどころを理解する。 | https://docs.python.org/3/library/itertools.html |
| `123_dataclass_deep` | `frozen`と`default_factory`で値とmutable defaultを正しく扱う。 | https://docs.python.org/3/library/dataclasses.html |
| `124_context_manager_deep` | `with`でresourceの開始・終了・復元を安全に扱う。 | https://docs.python.org/3/library/contextlib.html |
| `125_typing_extras` | `Literal`、`NewType`、`cast`で型の意図と限界を理解する。 | https://docs.python.org/3/library/typing.html |
| `126_import_module_deep` | public/private、`__all__`、循環importを読めるようにする。 | https://docs.python.org/3/tutorial/modules.html |
| `127_regex_practical` | validation、extract、replaceの用途別に正規表現を書く。 | https://docs.python.org/3/library/re.html |
| `128_algorithm_complexity` | 探索、sort、set利用で計算量を意識した処理を書く。 | https://docs.python.org/3/howto/sorting.html |
| `129_error_design_deep` | retryable/permanent errorを分け、握りつぶさない例外設計を学ぶ。 | https://docs.python.org/3/tutorial/errors.html |
| `130_fastapi_middleware_lifespan` | API横断処理、CORS、起動終了時のresource管理を分けて考える。 | https://fastapi.tiangolo.com/tutorial/middleware/ |
| `131_fastapi_files_websocket` | upload検証、ファイル名安全化、WebSocket message形式を決める。 | https://fastapi.tiangolo.com/advanced/websockets/ |
| `132_auth_jwt_rbac` | 認証token、JWT claim、role/action認可を分けて扱う。 | https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/ |
| `133_mongo_ops_schema` | index候補、schema validation、slow queryを運用目線で読む。 | https://www.mongodb.com/docs/manual/indexes/ |
| `134_worker_dead_letter` | retry上限、backoff、dead letter queueで失敗を管理する。 | https://docs.celeryq.dev/en/stable/userguide/tasks.html#retrying |
| `135_data_analysis_stats` | 平均だけでなく中央値と外れ値を見て分析判断をする。 | https://pandas.pydata.org/docs/ |
| `136_ai_dataset_versioning` | AI datasetはfingerprint、review状態、label分布を追跡する。 | https://www.nist.gov/itl/ai-risk-management-framework |
| `137_ai_ab_drift` | A/B testとdrift検知でAI変更の影響を見る。 | https://developers.google.com/machine-learning/crash-course/production-ml-systems |
| `138_rag_ops_quality` | RAGはreindex、search log、回答不能判定まで運用する。 | https://python.langchain.com/docs/concepts/retrieval/ |
| `139_security_scanning` | secret、dependency、permission leakをrelease前に確認する。 | https://owasp.org/www-project-top-ten/ |
| `140_observability_slo` | error rate、burn rate、latencyでSLOを監視する。 | https://sre.google/sre-book/service-level-objectives/ |
| `141_deploy_release_strategy` | canary、blue/green、rollback条件を先に決める。 | https://martinfowler.com/bliki/BlueGreenDeployment.html |
| `142_api_compatibility_design` | field削除やrequired追加を破壊的変更として扱う。 | https://spec.openapis.org/oas/latest.html |
