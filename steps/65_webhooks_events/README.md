# 65 Webhooks Events

## 学ぶこと

- webhook署名検証を理解する
- event_idで二重処理を防ぐ
- event drivenな処理をserviceへ渡す

## 書くこと

- HMAC署名を作る
- 署名を安全に比較する
- 処理済みeventをskipする

## 注意点

- 署名検証前にpayloadを信用しない
- 同じeventが複数回来ても壊れないようにする
- timestamp検証も本番では必要になる

## 参考URL

- https://docs.python.org/3/library/hmac.html

```bash
pytest steps/65_webhooks_events/tests -q
```

