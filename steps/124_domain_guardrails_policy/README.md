# 118 Domain Guardrails Policy

## 学ぶこと

- 特化型AIは対象外質問を断る設計が必要
- domain allowlist、PII、禁止行為をpolicy化する
- 拒否文もプロダクト品質の一部

## 書くこと

- domain外を判定する
- policy violationを返す
- 安全な拒否文を作る

## 参考URL

- https://owasp.org/www-project-top-10-for-large-language-model-applications/

```bash
pytest steps/124_domain_guardrails_policy/tests -q
```

