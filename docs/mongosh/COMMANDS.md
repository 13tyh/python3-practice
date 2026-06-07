# Mongosh Commands

## 接続

```bash
docker compose exec mongo mongosh
```

seed を再投入:

```bash
docker compose exec mongo mongosh /docker-entrypoint-initdb.d/01_seed.js
```

初期データ確認:

```javascript
use python_master
show collections
db.users.find({}, { _id: 0 }).limit(5)
db.municipalities.find({}, { _id: 0 })
db.groups.find({}, { _id: 0 })
db.subscriptions.find({}, { _id: 0 })
db.orders.find({}, { _id: 0 }).limit(5)
db.model_deployments.find({}, { _id: 0 })
db.rag_chunks.find({}, { _id: 0, chunk_id: 1, keywords: 1 })
db.batch_jobs.find({}, { _id: 0 })
```

## DB / Collection

```javascript
show dbs
use python_master
db
show collections
db.createCollection("users")
db.users.drop()
db.dropDatabase()
```

## Insert

```javascript
db.users.insertOne({ name: "Aki", role: "admin", score: 92 })

db.users.insertMany([
  { name: "Ren", role: "member", score: 75 },
  { name: "Mio", role: "member", score: 88 }
])
```

## Find

```javascript
db.users.find()
db.users.findOne()
db.users.find({ role: "member" })
db.users.find({ score: { $gte: 80 } })
db.users.find({ score: { $gte: 70, $lte: 90 } })
db.users.find({ name: /A/ })
db.users.find({ role: { $in: ["admin", "member"] } })
db.users.find({ deleted_at: { $exists: false } })
```

## Projection

```javascript
db.users.find({}, { _id: 0, name: 1, score: 1 })
db.users.find({ role: "member" }, { _id: 0, name: 1 })
```

## Sort / Limit / Skip

```javascript
db.users.find().sort({ score: -1 })
db.users.find().sort({ score: -1 }).limit(2)
db.users.find().sort({ score: -1 }).skip(2).limit(2)
```

## Count

```javascript
db.users.countDocuments()
db.users.countDocuments({ role: "member" })
db.users.estimatedDocumentCount()
```

## Update

```javascript
db.users.updateOne(
  { name: "Ren" },
  { $set: { score: 82 } }
)

db.users.updateMany(
  { role: "member" },
  { $inc: { score: 1 } }
)

db.users.updateOne(
  { name: "Sora" },
  { $set: { role: "member", score: 70 } },
  { upsert: true }
)
```

## Delete

```javascript
db.users.deleteOne({ name: "Sora" })
db.users.deleteMany({ score: { $lt: 50 } })
```

本番で `deleteMany({})` は危険。実行前に必ず条件と件数を見る。

```javascript
db.users.countDocuments({ score: { $lt: 50 } })
```

## Aggregation

```javascript
db.users.aggregate([
  { $match: { role: "member" } },
  { $group: { _id: "$role", avgScore: { $avg: "$score" }, count: { $sum: 1 } } },
  { $sort: { avgScore: -1 } }
])
```

```javascript
db.orders.aggregate([
  { $group: { _id: "$user_id", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } }
])
```

## Lookup

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "users",
      localField: "user_id",
      foreignField: "user_id",
      as: "user"
    }
  },
  { $unwind: "$user" }
])
```

## Index

```javascript
db.users.getIndexes()
db.users.createIndex({ score: -1 })
db.users.createIndex({ role: 1, score: -1 })
db.users.dropIndex({ score: -1 })
```

## Explain

```javascript
db.users.find({ score: { $gte: 80 } }).explain()
db.users.find({ score: { $gte: 80 } }).explain("executionStats")
```

見るポイント:

- `COLLSCAN`: 全件走査
- `IXSCAN`: index scan
- `totalDocsExamined`
- `totalKeysExamined`
- `executionTimeMillis`

## ObjectId / Date

```javascript
db.users.findOne({ _id: ObjectId("000000000000000000000000") })
db.logs.find({ created_at: { $gte: ISODate("2026-01-01T00:00:00Z") } })
```

## Bulk Write

```javascript
db.users.bulkWrite([
  { updateOne: { filter: { name: "Aki" }, update: { $set: { score: 95 } } } },
  { updateOne: { filter: { name: "Ren" }, update: { $set: { score: 82 } } } }
])
```
