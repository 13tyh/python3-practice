# 74 Settings And Secrets

## 学ぶこと

- 必須設定とsecretを分ける
- ログにsecretを出さない
- 設定不足を起動時に落とす

## 書くこと

- 必須keyを検証する
- secretをmaskする
- 公開してよい設定だけ返す

## 参考URL

- https://12factor.net/config

```bash
pytest exercise_tests/settings_secrets -q
```
