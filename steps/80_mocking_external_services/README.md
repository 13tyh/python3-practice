# 80 Mocking External Services

## 学ぶこと

- 外部APIをfake clientに置き換える
- 呼び出し履歴を検証する
- ネットワークなしでテストする

## 書くこと

- fake responseを返す
- call履歴を保存する
- 未登録URLを失敗させる

## 参考URL

- https://docs.pytest.org/en/stable/how-to/monkeypatch.html

```bash
pytest steps/80_mocking_external_services/tests -q
```

