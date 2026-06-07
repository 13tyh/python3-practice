# Expected Points

- API key を直書きしている
- router に DB、AI、ログが全部ある
- request / response schema がない
- `dict` で型が弱い
- `data["code"]` で KeyError
- secret を DB に保存している
- `print` を使っている
- Mongo の接続先が設定化されていない
- 例外処理がない
- テストしにくい

