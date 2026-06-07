"""悪い例: router に全部書いている。"""

from fastapi import APIRouter

router = APIRouter()


@router.post("/review")
def review(payload: dict[str, str]) -> dict[str, object]:
    api_key = "hard-coded-secret"
    prompt = "review this code: " + payload["code"]
    result = {"text": "ok", "api_key": api_key, "prompt": prompt}
    return result
