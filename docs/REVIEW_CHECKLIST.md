# Review Checklist

AI が書いたコード、または自分のコードを見る時のチェック。

## Python

- 型ヒントは嘘をついていないか
- `None` の可能性を扱っているか
- mutable default argument を使っていないか
- 例外を握りつぶしていないか
- ファイル encoding が明示されているか

## FastAPI

- router に業務ロジックが寄りすぎていないか
- request / response schema が分かれているか
- HTTP status code が適切か
- 404 / 400 / 500 の扱いがあるか
- TestClient で主要 flow を確認しているか

## AI

- prompt がテスト可能な関数か
- model 名を設定で変えられるか
- API key をログに出していないか
- AI の返答が空、長すぎる、不正形式の時を扱っているか
- fake client でテストできるか

## Logging

- `print` ではなく logger か
- `logger.exception` を使うべき箇所か
- secret を mask しているか
- 調査に必要な ID が残っているか

