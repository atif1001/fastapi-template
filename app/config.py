from typing import Optional
from functools import lru_cache

from pydantic import BaseSettings


# Load config settings
class Settings(BaseSettings):
    app_name: str = 'FastAPI Template'
    environment: str
    admin_email: Optional[str]

    class Config:
        env_file = ".env"


# Use caching for config settings
@lru_cache()
def get_settings():
    return Settings()
