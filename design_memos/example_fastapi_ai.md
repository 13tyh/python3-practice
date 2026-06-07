# Example FastAPI AI

## 変更内容

FastAPI でコードレビュー API を作る。

## なぜこの責務分けか

router は HTTP 入出力だけにする。prompt 作成と AI 呼び出しは service に置く。

## なぜこの型か

request / response を Pydantic model にして、API の契約を明確にする。

## なぜこの例外か

入力不正は 422 / 400、存在しない ID は 404、外部 AI 失敗は 502 に寄せる。

## なぜこのテストか

AI 本体は fake にして、API の契約と service の整形だけを安定して確認する。

