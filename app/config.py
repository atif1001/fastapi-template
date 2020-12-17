from typing import Optional
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'FastAPI Template'
    environment: str
    admin_email: Optional[str]

    class Config:
        env_file = ".env"


# Loading config settings
@lru_cache()
def get_settings():
    return Settings()
