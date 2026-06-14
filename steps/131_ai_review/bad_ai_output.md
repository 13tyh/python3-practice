# Bad AI Output

以下は AI が出しがちな危ない修正例です。すぐ貼らず、問題点を書き出してください。

```python
def find_user_email(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user["email"]
    return None
```

## 見るポイント

- 型ヒントが消えている
- 見つからない時の仕様が `ValueError` から `None` に変わっている
- `user["id"]` で `KeyError` の可能性がある
- 既存テストの期待と合っているか確認していない

