from functools import lru_cache

from pydantic import BaseSettings
from starlette.config import Config

config = Config(".env")


class AppSettings(BaseSettings):
    DATABASE_URL: str = config(
        "DATABASE_URL",
        cast=str,
        default="postgresql+asyncpg://postgres:postgres@localhost:55499/postgres",
    )
    DEBUG: bool = config("DEBUG", cast=bool, default=True)


@lru_cache()
def get_app_settings() -> AppSettings:
    return AppSettings()
