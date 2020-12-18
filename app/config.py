from typing import Optional
from functools import lru_cache

from pydantic import BaseSettings


# Load config settings
class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str = 'FastAPI Template'
    PORT: int

    class Config:
        env_file = ".env"


# Use caching for config settings
@lru_cache()
def get_settings():
    return Settings()
