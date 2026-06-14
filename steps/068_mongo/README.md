# 31 Mongo

対象: `src/mastery/mongo_practice.py`

## mongosh

```javascript
use python_master
db.users.find()
db.users.find({ score: { $gte: 80 } })
db.users.updateOne({ name: "Ren" }, { $set: { score: 82 } })
db.users.createIndex({ score: -1 })
```

## Python

```bash
python -c "from mastery.mongo_practice import seed_users, find_high_score_users; seed_users(); print(find_high_score_users(80))"
```

## 判断ポイント

- `_id` を返す必要があるか
- index が必要な検索か
- `delete_many({})` を本番で使ってよいか
- DB 接続情報をコードに直書きしていないか


