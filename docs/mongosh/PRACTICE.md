# Mongosh Practice

## Seed

Docker 初回起動時は `docker/mongo-init/01_seed.js` が自動実行されます。
再投入したい場合:

```bash
docker compose exec mongo mongosh /docker-entrypoint-initdb.d/01_seed.js
```

手で seed する場合:

```javascript
use python_master

db.users.deleteMany({})
db.orders.deleteMany({})

db.users.insertMany([
  { user_id: "u1", name: "Aki", role: "admin", score: 92 },
  { user_id: "u2", name: "Ren", role: "member", score: 75 },
  { user_id: "u3", name: "Mio", role: "member", score: 88 }
])

db.orders.insertMany([
  { order_id: "o1", user_id: "u1", amount: 1200, status: "paid" },
  { order_id: "o2", user_id: "u2", amount: 800, status: "paid" },
  { order_id: "o3", user_id: "u2", amount: 300, status: "cancelled" },
  { order_id: "o4", user_id: "u3", amount: 1500, status: "paid" }
])
```

## Practice 1: 基本検索

```javascript
db.users.find({ role: "member" })
db.users.find({ score: { $gte: 80 } }, { _id: 0, name: 1, score: 1 })
db.users.find().sort({ score: -1 }).limit(2)
```

## Practice 2: 更新

```javascript
db.users.updateOne(
  { user_id: "u2" },
  { $set: { score: 82 } }
)

db.users.find({ user_id: "u2" })
```

## Practice 3: 集計

```javascript
db.orders.aggregate([
  { $match: { status: "paid" } },
  { $group: { _id: "$user_id", total: { $sum: "$amount" }, count: { $sum: 1 } } },
  { $sort: { total: -1 } }
])
```

## Practice 4: Join 的処理

```javascript
db.orders.aggregate([
  { $match: { status: "paid" } },
  {
    $lookup: {
      from: "users",
      localField: "user_id",
      foreignField: "user_id",
      as: "user"
    }
  },
  { $unwind: "$user" },
  {
    $project: {
      _id: 0,
      order_id: 1,
      amount: 1,
      user_name: "$user.name"
    }
  }
])
```

## Practice 5: Index と explain

```javascript
db.orders.createIndex({ status: 1, user_id: 1 })
db.orders.find({ status: "paid", user_id: "u2" }).explain("executionStats")
```

## Practice 6: RAG 用 document / chunk 検索

```javascript
db.documents.find({ tags: "rag" }, { _id: 0, title: 1, text: 1 })
db.rag_chunks.find({ keywords: "fastapi" }, { _id: 0, chunk_id: 1, content: 1 })
```

## Practice 7: deployment_name から model_name を引く

```javascript
db.model_deployments.findOne(
  { deployment_name: "review-fast", active: true },
  { _id: 0, deployment_name: 1, model_name: 1, provider: 1 }
)
```

## Practice 8: バッチ推論の状態確認

```javascript
db.batch_jobs.find(
  { status: { $in: ["running", "failed"] } },
  { _id: 0, job_id: 1, status: 1, success_count: 1, error_count: 1 }
)
```

## Practice 9: 問い合わせを優先度別に集計

```javascript
db.support_tickets.aggregate([
  { $match: { status: "open" } },
  { $group: { _id: "$priority", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
])
```

## Practice 10: 自治体ごとの契約状態

```javascript
db.subscriptions.aggregate([
  {
    $lookup: {
      from: "municipalities",
      localField: "municipality_id",
      foreignField: "municipality_id",
      as: "municipality"
    }
  },
  { $unwind: "$municipality" },
  {
    $project: {
      _id: 0,
      municipality_name: "$municipality.name",
      prefecture: "$municipality.prefecture",
      plan: 1,
      status: 1,
      seats: 1,
      monthly_fee: 1
    }
  }
])
```

## Practice 11: group 所属ユーザーを探す

```javascript
db.users.find(
  { group_ids: "g-reviewer", active: true },
  { _id: 0, user_id: 1, name: 1, municipality_id: 1, group_ids: 1 }
)
```

## Practice 12: 自治体ごとの active user 数

```javascript
db.users.aggregate([
  { $match: { active: true } },
  { $group: { _id: "$municipality_id", active_users: { $sum: 1 } } },
  {
    $lookup: {
      from: "municipalities",
      localField: "_id",
      foreignField: "municipality_id",
      as: "municipality"
    }
  },
  { $unwind: "$municipality" },
  { $project: { _id: 0, municipality: "$municipality.name", active_users: 1 } },
  { $sort: { active_users: -1 } }
])
```
