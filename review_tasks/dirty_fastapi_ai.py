from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://mongo:27017")
db = client.app


@app.post("/ai/review")
def review(data: dict):
    key = "secret"
    code = data["code"]
    result = "ok: " + code
    db.logs.insert_one({"code": code, "key": key, "result": result})
    print("reviewed", data)
    return {"result": result}

