# Bad AI Output

AI が出しがちな修正:

```python
def create_user(payload):
    if not payload["name"]:
        return {"error": "name required"}
    db.users.insert_one(payload)
    return payload
```

## 問題

- 型がない
- request schema がない
- DB 例外がそのまま
- `_id` が JSON 化できない可能性
- password や secret を保存する危険
- service / repository に分かれていない

