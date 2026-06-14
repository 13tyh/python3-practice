# 132 Auth JWT RBAC

## 学ぶこと

- Bearer tokenの取り出し
- JWT claimの基本
- RBACでroleとactionを分ける

## 書くこと

- headerからtokenを読む
- roleのpermissionを判定する
- expを使って期限切れを判定する

## 参考URL

- https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

```bash
pytest steps/132_auth_jwt_rbac/tests -q
```

