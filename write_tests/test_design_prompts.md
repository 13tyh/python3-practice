# Test Design Prompts

テストを書く前に答える。

## 何を守るテストか

例: API key がログやレスポンスに出ないこと。

## どの入力で壊れるか

例: `code` が空、`focus` が未知、AI の返答が空。

## 期待値は何か

例: 400 を返す、空の suggestions にする、logger.exception が呼ばれる。

