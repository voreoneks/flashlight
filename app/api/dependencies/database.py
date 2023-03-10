from typing import Callable, Type

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.base import BaseRepository
from app.db.setup import async_session


async def _get_session() -> AsyncSession:
    async with async_session.begin() as session:
        session: AsyncSession
        yield session


def get_repository(
    repo_type: Type[BaseRepository],
) -> Callable[[AsyncSession], BaseRepository]:
    async def _get_repo(
        session: AsyncSession = Depends(_get_session),
    ) -> BaseRepository:
        return repo_type(session)

    return _get_repo
