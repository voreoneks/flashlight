from asyncio import AbstractEventLoop
from typing import AsyncGenerator, Callable
import asyncio
import platform

from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncConnection
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import scoped_session, sessionmaker
import pytest_asyncio

from app.core.settings import AppSettings, get_app_settings
from app.db.tables import get_metadata
from tests.fixtures import *
from tests.mock import *


@pytest_asyncio.fixture(scope="session")
def app_config() -> AppSettings:
    return get_app_settings()


@pytest_asyncio.fixture(scope="session")
def map_models():
    yield get_metadata()


@pytest_asyncio.fixture(scope="session")
def event_loop() -> AbstractEventLoop:
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    return asyncio.new_event_loop()


@pytest_asyncio.fixture
async def connection(app_config: AppSettings) -> AsyncConnection:
    engine = create_async_engine(app_config.DATABASE_URL, echo=False, future=True)
    metadata = get_metadata()

    async with engine.begin() as connection:
        connection: AsyncConnection
        await connection.run_sync(metadata.drop_all)
        await connection.run_sync(metadata.create_all)
        yield connection


@pytest_asyncio.fixture
async def db_session(connection) -> AsyncSession:
    async_session = sessionmaker(
        connection, expire_on_commit=False, class_=AsyncSession
    )
    async with scoped_session(async_session)() as session:
        session: AsyncSession
        yield session
        await session.rollback()


@pytest_asyncio.fixture
def get_session(db_session: AsyncSession):
    async def _override_get_session():
        yield db_session

    return _override_get_session


@pytest_asyncio.fixture
def app(get_session: Callable) -> FastAPI:
    from app.api.dependencies.database import _get_session
    from app.main import app

    app.dependency_overrides[_get_session] = get_session

    return app


@pytest_asyncio.fixture
async def async_client(app: FastAPI) -> AsyncGenerator:
    async with AsyncClient(
        app=app, base_url=f"http://127.0.0.1:8000"
    ) as async_client:
        yield async_client
