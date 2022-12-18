from functools import lru_cache

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:postgres@localhost:55499/postgres"
    )
    DEBUG: bool = True


@lru_cache()
def get_app_settings() -> AppSettings:
    return AppSettings()
