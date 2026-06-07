import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    mongo_uri: str
    database: str
    ai_provider: str
    ai_model: str


def load_settings() -> Settings:
    return Settings(
        mongo_uri=os.getenv("MONGO_URI", "mongodb://mongo:27017"),
        database=os.getenv("MONGO_DATABASE", "ai_review"),
        ai_provider=os.getenv("AI_PROVIDER", "fake"),
        ai_model=os.getenv("AI_MODEL", "fake-reviewer"),
    )

