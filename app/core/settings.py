from pydantic import BaseSettings
from starlette.config import Config
from functools import lru_cache

config = Config('.env')

class AppSettings(BaseSettings):
    DATABASE_URL: str = config(
        'DATABASE_URL',
        cast=str,
        default='postgresql+asyncpg://postgres:postgres@localhost:55499/postgres'
    )

@lru_cache()
def get_app_settings() -> AppSettings:
    return AppSettings()